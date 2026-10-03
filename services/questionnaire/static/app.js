const T = {
  en: {
    title: "Questionnaire",
    privacy: "Do not include your name, your employer, client names, project names, or system names.",
    next: "Next",
    back: "Back",
    save: "Save",
    review: "Review",
    submit: "Submit",
    submitted: "Submitted",
    yourId: "Participant ID",
    download: "Download the file",
    record: "Record",
    stop: "Stop",
    recording: "Recording",
    working: "Transcribing",
    editHint: "Words appear in this box as the recording is transcribed. Save tidies punctuation and line breaks. Change the text if it does not match what you said.",
    formatted: "Saved. Punctuation and line breaks were tidied. The words were not rewritten.",
    heardNone: "No speech was heard. Record again, or type the answer.",
    skip: "Skip",
    required: "Answer this question, or skip it.",
    saved: "Saved. You can close this page and return with the same address.",
    done: "The answers are stored under this ID. The file does not contain your name or sign-in.",
    micError: "The microphone is not available. You can type the answer.",
    speechWait: "The speech service is still starting. Try the recording again in a minute.",
    speechDown: "Transcription did not finish. You can type the answer.",
    otherPh: "Write the other answer",
    of: "of",
    begin: "Begin"
  },
  ru: {
    title: "Опросник",
    privacy: "Не указывайте своё имя, работодателя, названия клиентов, проектов или систем.",
    next: "Дальше",
    back: "Назад",
    save: "Сохранить",
    review: "Просмотр",
    submit: "Отправить",
    submitted: "Отправлено",
    yourId: "Номер участника",
    download: "Скачать файл",
    record: "Запись",
    stop: "Стоп",
    recording: "Идёт запись",
    working: "Распознавание",
    editHint: "Слова появляются в этом поле по ходу распознавания. Сохранение поправляет знаки и абзацы. Исправьте текст, если он не совпадает с тем, что вы сказали.",
    formatted: "Сохранено. Знаки и абзацы поправлены. Слова не переписывались.",
    heardNone: "Речь не распознана. Запишите ещё раз или введите ответ.",
    skip: "Пропустить",
    required: "Ответьте на вопрос или пропустите его.",
    saved: "Сохранено. Эту страницу можно закрыть и открыть снова по тому же адресу.",
    done: "Ответы сохранены под этим номером. В файле нет вашего имени и данных входа.",
    micError: "Микрофон недоступен. Ответ можно ввести текстом.",
    speechWait: "Сервис речи ещё запускается. Повторите запись через минуту.",
    speechDown: "Распознавание не завершилось. Ответ можно ввести текстом.",
    otherPh: "Напишите другой ответ",
    of: "из",
    begin: "Начать"
  },
  he: {
    title: "שאלון",
    privacy: "אל תכללו את שמכם, את המעסיק, שמות לקוחות, שמות פרויקטים או שמות מערכות.",
    next: "הבא",
    back: "הקודם",
    save: "שמירה",
    review: "סקירה",
    submit: "שליחה",
    submitted: "נשלח",
    yourId: "מזהה משתתף",
    download: "הורדת הקובץ",
    record: "הקלטה",
    stop: "עצירה",
    recording: "מקליט",
    working: "תמלול",
    editHint: "המילים מופיעות בתיבה תוך כדי התמלול. שמירה מסדרת פיסוק ומעברי שורה. תקנו את הטקסט אם הוא לא תואם למה שאמרתם.",
    formatted: "נשמר. הפיסוק ומעברי השורה סודרו. המילים לא נכתבו מחדש.",
    heardNone: "לא נקלט דיבור. הקליטו שוב, או הקלידו את התשובה.",
    skip: "דילוג",
    required: "ענו על השאלה, או דלגו עליה.",
    saved: "נשמר. אפשר לסגור את הדף ולחזור לאותה כתובת.",
    done: "התשובות נשמרו תחת המזהה הזה. בקובץ אין שם ואין פרטי כניסה.",
    micError: "המיקרופון לא זמין. אפשר להקליד את התשובה.",
    speechWait: "שירות הדיבור עדיין עולה. נסו שוב בעוד דקה.",
    speechDown: "התמלול לא הושלם. אפשר להקליד את התשובה.",
    otherPh: "כתבו את התשובה האחרת",
    of: "מתוך",
    begin: "התחלה"
  }
};

const params = new URLSearchParams(location.search);
let lang = ["en", "ru", "he"].includes(params.get("lang")) ? params.get("lang") : "en";
let instrument = null;
let session = null;
let index = 0;
let status = "";
let recorder = null;
let transcribeChain = Promise.resolve();
let heardSegments = {};
let lastRaw = {};
const appEl = document.getElementById("app");

function t() { return T[lang]; }
function tx(bag) { return (bag && (bag[lang] || bag.en)) || ""; }
function sections() { return instrument.sections.filter((section) => !section.interviewer || session.interviewer); }

function visible(question) {
  if (question.interviewer && !session.interviewer) return false;
  if (!question.showIf) return true;
  const current = answer(question.showIf.question);
  return !current.skipped && current.choice.includes(question.showIf.includes);
}

function questions() {
  return sections().flatMap((section) => section.questions.filter(visible).map((question) => ({ section, question })));
}

function applyDir() {
  document.documentElement.lang = lang;
  document.documentElement.dir = lang === "he" ? "rtl" : "ltr";
  document.getElementById("title").textContent = t().title;
}

function answer(id) {
  return (session.answers && session.answers[id]) || { text: "", choice: [], other: "", skipped: false };
}

async function api(path, options) {
  const response = await fetch(path, options);
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    const error = new Error("request failed");
    error.status = response.status;
    error.body = data;
    throw error;
  }
  return data;
}

async function persist() {
  session = await api("/api/sessions/" + session.id, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ lang, step: index, answers: session.answers })
  });
  const url = new URL(location.href);
  url.searchParams.set("id", session.id);
  url.searchParams.set("lang", lang);
  history.replaceState(null, "", url);
}

function setAnswer(id, patch) {
  session.answers[id] = Object.assign(answer(id), patch, { skipped: false });
}

function langs() {
  return ["en", "ru", "he"].map((code) => {
    const name = { en: "English", ru: "Русский", he: "עברית" }[code];
    return `<button type="button" data-lang="${code}" class="${code === lang ? "on" : ""}">${name}</button>`;
  }).join("");
}

function shell(inner) {
  appEl.innerHTML = inner + `<p class="status">${status}</p>`;
}

function progress(current, total) {
  const width = total ? Math.round((current / total) * 100) : 0;
  return `<div class="progress" aria-hidden="true"><span style="width:${width}%"></span></div>`;
}

async function begin() {
  session = await api("/api/sessions", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      lang,
      interviewer: params.get("mode") === "interviewer",
      id: params.get("id") || ""
    })
  });
  lang = session.lang || lang;
  index = Math.min(session.step || 0, Math.max(0, questions().length));
  if (session.status === "submitted") renderDone();
  else if (index >= questions().length && questions().length) renderReview();
  else renderQuestion();
}

function renderQuestion() {
  applyDir();
  const flat = questions();
  if (!flat.length) return;
  if (index >= flat.length) return renderReview();
  if (index < 0) index = 0;
  const { section, question } = flat[index];
  const current = answer(question.id);
  let field = "";
  if (question.type === "text") {
    field = `<textarea id="text" data-qid="${question.id}">${escapeHtml(current.text)}</textarea>`;
  } else {
    const input = question.type === "multi" ? "checkbox" : "radio";
    field = question.options.map((option) => `
      <label class="option">
        <input type="${input}" name="choice" value="${option.id}" ${current.choice.includes(option.id) ? "checked" : ""}>
        <span>${escapeHtml(tx(option.label))}</span>
      </label>
    `).join("");
    const otherOn = question.options.some((option) => option.other && current.choice.includes(option.id));
    field += `<input id="other" type="text" placeholder="${escapeHtml(t().otherPh)}" value="${escapeHtml(current.other)}" ${otherOn ? "" : "hidden"}>`;
  }
  const probe = question.probe && session.interviewer ? `<p class="probe">${escapeHtml(tx(question.probe))}</p>` : "";
  const lead = section.lead ? `<p class="lead">${escapeHtml(tx(section.lead))}</p>` : "";
  shell(`
    ${progress(index + 1, flat.length + 1)}
    <article class="card">
      <p class="kicker">${escapeHtml(question.code)} · ${index + 1} ${t().of} ${flat.length}</p>
      <h2>${escapeHtml(tx(section.title))}</h2>
      ${lead}
      <p class="prompt">${escapeHtml(tx(question.prompt))}</p>
      ${probe}
      ${field}
      <p class="note">${question.voice ? t().editHint : ""}</p>
      <p class="note">${t().privacy}</p>
      <div class="langs">${langs()}</div>
      <div class="row">
        ${index ? `<button type="button" class="secondary" id="back">${t().back}</button>` : ""}
        ${question.voice ? `<button type="button" class="record" id="record">${t().record}</button>` : ""}
        <button type="button" class="secondary" id="skip">${t().skip}</button>
        <button type="button" class="secondary" id="save">${t().save}</button>
        <button type="button" id="next">${index === flat.length - 1 ? t().review : t().next}</button>
      </div>
    </article>
  `);
  bindCommon(flat);
  const text = document.getElementById("text");
  if (text) text.oninput = () => setAnswer(question.id, { text: text.value });
  appEl.querySelectorAll("input[name=choice]").forEach((input) => {
    input.onchange = () => collectChoice(question);
  });
  const other = document.getElementById("other");
  if (other) other.oninput = () => setAnswer(question.id, { other: other.value });
  const record = document.getElementById("record");
  if (record) record.onclick = () => toggleRecord(question.id, record);
  document.getElementById("skip").onclick = async () => {
    session.answers[question.id] = { text: "", choice: [], other: "", skipped: true };
    await persist();
    index += 1;
    renderQuestion();
  };
  document.getElementById("next").onclick = async () => {
    if (recorder) await recorder.stop();
    await transcribeChain;
    const box = document.getElementById("text");
    collectChoice(question);
    if (box) setAnswer(question.id, { text: box.value });
    if (!filled(question)) {
      status = status || t().required;
      renderQuestion();
      return;
    }
    status = "";
    await persist();
    index += 1;
    renderQuestion();
  };
}

function collectChoice(question) {
  if (question.type === "text") return;
  const choice = [...appEl.querySelectorAll("input[name=choice]:checked")].map((input) => input.value);
  const other = document.getElementById("other");
  const otherOn = question.options.some((option) => option.other && choice.includes(option.id));
  if (other) other.hidden = !otherOn;
  setAnswer(question.id, { choice, other: other ? other.value : "" });
}

function filled(question) {
  const current = answer(question.id);
  if (current.skipped) return true;
  if (question.type === "text") return current.text.trim().length > 0;
  if (question.type === "single" && current.choice.length !== 1) return false;
  if (question.type === "multi" && !current.choice.length) return false;
  return question.options.every((option) => !option.other || !current.choice.includes(option.id) || current.other.trim());
}

function bindCommon() {
  appEl.querySelectorAll("[data-lang]").forEach((button) => {
    button.onclick = async () => {
      const flat = questions();
      const text = document.getElementById("text");
      if (flat[index]) collectChoice(flat[index].question);
      if (text && flat[index]) setAnswer(flat[index].question.id, { text: text.value });
      lang = button.dataset.lang;
      await persist();
      renderQuestion();
    };
  });
  const back = document.getElementById("back");
  if (back) back.onclick = async () => { await persist(); index -= 1; renderQuestion(); };
  document.getElementById("save").onclick = async () => {
    if (recorder) await recorder.stop();
    await transcribeChain;
    const box = document.getElementById("text");
    const flat = questions();
    const current = flat[index] && flat[index].question;
    if (current) collectChoice(current);
    let value = box ? box.value : "";
    if (current && current.type === "text" && value.trim()) {
      const segments = heardSegments[current.id];
      const unchanged = normalize(value) === normalize(lastRaw[current.id] || "");
      const formatted = await api("/api/format", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: value,
          language: lang,
          segments: unchanged && segments ? segments : []
        })
      });
      value = formatted.text || value;
      if (box) box.value = value;
      lastRaw[current.id] = value;
    }
    if (current && current.type === "text") setAnswer(current.id, { text: value });
    await persist();
    status = value.trim() ? t().formatted : t().saved;
    renderQuestion();
  };
}

function renderReview() {
  applyDir();
  const flat = questions();
  const rows = flat.map(({ question }) => {
    const current = answer(question.id);
    let value = "—";
    if (!current.skipped && question.type === "text") value = current.text || "—";
    if (!current.skipped && question.type !== "text") {
      value = question.options
        .filter((option) => current.choice.includes(option.id))
        .map((option) => option.other && current.other ? current.other : tx(option.label))
        .join(", ") || "—";
    }
    return `<dt>${escapeHtml(question.code)} ${escapeHtml(tx(question.prompt))}</dt><dd>${escapeHtml(value)}</dd>`;
  }).join("");
  shell(`
    ${progress(flat.length + 1, flat.length + 1)}
    <article class="card">
      <h2>${t().review}</h2>
      <dl class="review">${rows}</dl>
      <div class="row">
        <button type="button" class="secondary" id="back">${t().back}</button>
        <button type="button" id="submit">${t().submit}</button>
      </div>
      <p class="note">${t().yourId}: ${session.id}</p>
    </article>
  `);
  document.getElementById("back").onclick = () => { index = Math.max(0, flat.length - 1); renderQuestion(); };
  document.getElementById("submit").onclick = send;
}

async function send() {
  document.getElementById("submit").disabled = true;
  try {
    await persist();
    const result = await api("/api/sessions/" + session.id + "/submit", { method: "POST" });
    session.status = "submitted";
    session.file = result.file;
    renderDone();
  } catch (error) {
    status = t().required;
    const missing = error.body && error.body.detail && error.body.detail.missing;
    if (missing) {
      const found = questions().findIndex((item) => item.question.id === missing[0]);
      if (found >= 0) {
        index = found;
        renderQuestion();
        return;
      }
    }
    renderReview();
  }
}

function renderDone() {
  applyDir();
  shell(`
    <article class="card">
      <h2>${t().submitted}</h2>
      <p>${t().done}</p>
      <p class="kicker">${t().yourId}</p>
      <p class="id">${session.id}</p>
      <div class="row"><a href="/api/sessions/${session.id}/file"><button type="button">${t().download}</button></a></div>
    </article>
  `);
}

function renderStart() {
  applyDir();
  shell(`
    <article class="card">
      <h2>${t().title}</h2>
      <p>${t().privacy}</p>
      <div class="langs">${langs()}</div>
      <div class="row"><button type="button" id="begin">${t().begin}</button></div>
    </article>
  `);
  appEl.querySelectorAll("[data-lang]").forEach((button) => {
    button.onclick = () => { lang = button.dataset.lang; renderStart(); };
  });
  document.getElementById("begin").onclick = begin;
}

function normalize(value) {
  return String(value || "").replace(/\s+/g, " ").trim();
}

function applyTranscript(questionId, text, segments) {
  setAnswer(questionId, { text: text || "" });
  lastRaw[questionId] = text || "";
  if (segments && segments.length) heardSegments[questionId] = segments;
  const box = document.getElementById("text");
  if (box && box.dataset.qid === questionId) box.value = text || "";
  const note = document.querySelector(".status");
  if (note) note.textContent = text ? "" : status;
}

function postAudio(wav) {
  const body = new FormData();
  body.append("file", new Blob([wav], { type: "audio/wav" }), "answer.wav");
  body.append("language", lang);
  const job = transcribeChain.then(() => api("/api/sessions/" + session.id + "/transcribe", { method: "POST", body }));
  transcribeChain = job.then(() => {}, () => {});
  return job;
}

async function toggleRecord(questionId, button) {
  if (recorder) return recorder.stop();
  let stream;
  try {
    stream = await navigator.mediaDevices.getUserMedia({ audio: { channelCount: 1, echoCancellation: true } });
  } catch (_err) {
    status = t().micError;
    renderQuestion();
    return;
  }
  const context = new AudioContext();
  await context.resume();
  const source = context.createMediaStreamSource(stream);
  const processor = context.createScriptProcessor(4096, 1, 1);
  const silent = context.createGain();
  silent.gain.value = 0;
  const chunks = [];
  const started = Date.now();
  const before = answer(questionId).text.trim();
  const sampleRate = context.sampleRate || 16000;
  let partialAt = 0;
  processor.onaudioprocess = (event) => {
    chunks.push(new Float32Array(event.inputBuffer.getChannelData(0)));
    const elapsed = Math.round((Date.now() - started) / 1000);
    if (button.isConnected) button.textContent = t().stop + " " + elapsed + "s";
    if (elapsed >= 55 && recorder) recorder.stop();
    if (elapsed - partialAt >= 8 && elapsed >= 3) {
      partialAt = elapsed;
      const wav = encodeWav(chunks.slice(), sampleRate);
      postAudio(wav).then((result) => {
        if (!result.text) return;
        const spoken = before ? before + "\n" + result.text : result.text;
        applyTranscript(questionId, spoken, result.segments);
      }).catch(() => {});
    }
  };
  source.connect(processor);
  processor.connect(silent);
  silent.connect(context.destination);
  button.classList.add("on");
  button.textContent = t().stop;
  status = t().recording;
  const note = document.querySelector(".status");
  if (note) note.textContent = status;
  let stopping = null;
  recorder = {
    stop: () => {
      if (stopping) return stopping;
      stopping = (async () => {
        recorder = null;
        processor.disconnect();
        source.disconnect();
        silent.disconnect();
        stream.getTracks().forEach((track) => track.stop());
        const rate = context.sampleRate || sampleRate;
        await context.close();
        if (button.isConnected) {
          button.disabled = true;
          button.textContent = t().working;
        }
        status = t().working;
        const live = document.querySelector(".status");
        if (live) live.textContent = status;
        const wav = encodeWav(chunks, rate);
        try {
          const result = await postAudio(wav);
          if (result.text) {
            applyTranscript(questionId, before ? before + "\n" + result.text : result.text, result.segments);
            status = "";
          } else {
            status = t().heardNone;
          }
        } catch (error) {
          status = error.status === 503 ? t().speechWait : t().speechDown;
        }
        renderQuestion();
      })();
      return stopping;
    }
  };
}

function encodeWav(chunks, sampleRate) {
  const length = chunks.reduce((sum, chunk) => sum + chunk.length, 0);
  const buffer = new ArrayBuffer(44 + length * 2);
  const view = new DataView(buffer);
  const write = (offset, text) => { for (let i = 0; i < text.length; i += 1) view.setUint8(offset + i, text.charCodeAt(i)); };
  write(0, "RIFF");
  view.setUint32(4, 36 + length * 2, true);
  write(8, "WAVE");
  write(12, "fmt ");
  view.setUint32(16, 16, true);
  view.setUint16(20, 1, true);
  view.setUint16(22, 1, true);
  view.setUint32(24, sampleRate, true);
  view.setUint32(28, sampleRate * 2, true);
  view.setUint16(32, 2, true);
  view.setUint16(34, 16, true);
  write(36, "data");
  view.setUint32(40, length * 2, true);
  let offset = 44;
  chunks.forEach((chunk) => {
    for (let i = 0; i < chunk.length; i += 1) {
      const sample = Math.max(-1, Math.min(1, chunk[i]));
      view.setInt16(offset, sample < 0 ? sample * 0x8000 : sample * 0x7fff, true);
      offset += 2;
    }
  });
  return buffer;
}

function escapeHtml(value) {
  return String(value).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

async function boot() {
  instrument = await api("/api/instrument");
  const existing = params.get("id");
  if (existing) {
    await begin();
    return;
  }
  renderStart();
}

boot();
