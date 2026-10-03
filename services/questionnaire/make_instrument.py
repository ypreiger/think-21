"""Build instrument.json from the GM965 questionnaire v1.4 participant questions."""

import json
from pathlib import Path


def t(en, ru, he):
    return {"en": en, "ru": ru, "he": he}


def opt(oid, en, ru, he, other=False):
    item = {"id": oid, "label": t(en, ru, he)}
    if other:
        item["other"] = True
    return item


def choice(qid, code, kind, en, ru, he, options, optional=True):
    return {
        "id": qid,
        "code": code,
        "type": kind,
        "voice": False,
        "optional": optional,
        "prompt": t(en, ru, he),
        "options": options,
    }


def textq(qid, code, en, ru, he, probe=None, optional=True):
    item = {
        "id": qid,
        "code": code,
        "type": "text",
        "voice": True,
        "optional": optional,
        "prompt": t(en, ru, he),
    }
    if probe:
        item["probe"] = probe
    return item


OTHER = opt("other", "Other", "Другое", "אחר", other=True)

instrument = {
    "id": "gm965-v1.4",
    "sections": [
        {
            "id": "role",
            "title": t(
                "About your professional role",
                "О вашей профессиональной роли",
                "על התפקיד המקצועי שלך",
            ),
            "questions": [
                choice(
                    "q1_1", "1.1", "single",
                    "What is your current role or position?",
                    "Какова ваша текущая роль или должность?",
                    "מהו התפקיד או המשרה הנוכחית שלך?",
                    [
                        opt("ceo", "CEO / Managing Director", "Генеральный директор", "מנכ״ל / מנהל כללי"),
                        opt("cto", "CTO / CIO / Head of IT", "Технический директор / ИТ-директор", "מנהל טכנולוגיות / מנהל מערכות מידע"),
                        opt("architect", "Architect", "Архитектор", "ארכיטקט"),
                        opt("engineer", "Technical specialist / Engineer", "Технический специалист / инженер", "מומחה טכני / מהנדס"),
                        opt("manager", "Manager / Team Lead", "Руководитель / руководитель команды", "מנהל / ראש צוות"),
                        opt("grc", "Governance / Risk / Compliance", "Управление, риски и соответствие", "ממשל / סיכון / ציות"),
                        opt("consultant", "Consultant / Advisor", "Консультант / советник", "יועץ"),
                        opt("business", "Business or operational role", "Бизнес-роль или операционная роль", "תפקיד עסקי או תפעולי"),
                        OTHER,
                    ],
                ),
                choice(
                    "q1_2", "1.2", "single",
                    "Which industry or sector best describes your organization?",
                    "Какая отрасль лучше всего описывает вашу организацию?",
                    "איזה ענף או מגזר מתאר הכי טוב את הארגון שלך?",
                    [
                        opt("banking", "Banking / Financial Services", "Банки / финансовые услуги", "בנקאות / שירותים פיננסיים"),
                        opt("technology", "Technology / Software / IT Services", "Технологии / программное обеспечение / ИТ-услуги", "טכנולוגיה / תוכנה / שירותי IT"),
                        opt("telecom", "Telecommunications", "Телекоммуникации", "תקשורת"),
                        opt("healthcare", "Healthcare", "Здравоохранение", "בריאות"),
                        opt("manufacturing", "Manufacturing", "Производство", "ייצור"),
                        opt("retail", "Retail / Consumer Services", "Розница / потребительские услуги", "קמעונאות / שירותים לצרכן"),
                        opt("public", "Public Sector", "Государственный сектор", "מגזר ציבורי"),
                        opt("education", "Education", "Образование", "חינוך"),
                        OTHER,
                    ],
                ),
                choice(
                    "q1_3", "1.3", "single",
                    "How many years of professional experience do you have?",
                    "Сколько лет у вас профессионального опыта?",
                    "כמה שנות ניסיון מקצועי יש לך?",
                    [
                        opt("lt5", "Less than 5 years", "Менее 5 лет", "פחות מ-5 שנים"),
                        opt("5_10", "5–10 years", "5–10 лет", "5–10 שנים"),
                        opt("11_20", "11–20 years", "11–20 лет", "11–20 שנים"),
                        opt("gt20", "More than 20 years", "Более 20 лет", "יותר מ-20 שנה"),
                        opt("other", "Other / prefer not to say", "Другое / предпочитаю не указывать", "אחר / מעדיף לא לציין", other=True),
                    ],
                ),
                choice(
                    "q1_4", "1.4", "single",
                    "How often do you use, review, or receive AI-assisted information in your professional work?",
                    "Как часто вы используете, проверяете или получаете информацию с помощью ИИ в профессиональной работе?",
                    "באיזו תדירות אתה משתמש, בודק או מקבל מידע שנעזר בבינה מלאכותית בעבודה המקצועית?",
                    [
                        opt("daily", "Daily", "Ежедневно", "כל יום"),
                        opt("weekly", "Several times a week", "Несколько раз в неделю", "כמה פעמים בשבוע"),
                        opt("monthly", "Several times a month", "Несколько раз в месяц", "כמה פעמים בחודש"),
                        opt("occasionally", "Occasionally", "Время от времени", "מדי פעם"),
                        opt("rarely", "Rarely", "Редко", "לעיתים רחוקות"),
                        OTHER,
                    ],
                ),
                choice(
                    "q1_5", "1.5", "multi",
                    "For which types of work do you use or receive AI-assisted information? Select every item that applies.",
                    "Для каких видов работы вы используете или получаете информацию с помощью ИИ? Отметьте всё подходящее.",
                    "לאילו סוגי עבודה אתה משתמש או מקבל מידע שנעזר בבינה מלאכותית? סמן כל מה שמתאים.",
                    [
                        opt("analysis", "Analysis or research", "Анализ или исследование", "ניתוח או מחקר"),
                        opt("design", "Technical design or architecture", "Техническое проектирование или архитектура", "תכנון טכני או ארכיטקטורה"),
                        opt("decision", "Decision support", "Поддержка решений", "תמיכה בהחלטות"),
                        opt("writing", "Writing or documentation", "Тексты или документация", "כתיבה או תיעוד"),
                        opt("software", "Software development", "Разработка программного обеспечения", "פיתוח תוכנה"),
                        opt("operations", "Operations or troubleshooting", "Эксплуатация или поиск неисправностей", "תפעול או איתור תקלות"),
                        opt("planning", "Planning or strategy", "Планирование или стратегия", "תכנון או אסטרטגיה"),
                        opt("client", "Customer or client communication", "Общение с заказчиком или клиентом", "תקשורת עם לקוח"),
                        OTHER,
                    ],
                ),
                choice(
                    "q1_6", "1.6", "single",
                    "Which side of the IT relationship are you mainly on?",
                    "На какой стороне ИТ-отношений вы в основном находитесь?",
                    "באיזה צד של קשר ה-IT אתה נמצא בעיקר?",
                    [
                        opt("vendor", "Vendor, integrator or consultancy providing IT products or services to clients", "Поставщик, интегратор или консультант, который предоставляет клиентам ИТ-продукты или услуги", "ספק, אינטגרטור או ייעוץ שמספקים ללקוחות מוצרי IT או שירותים"),
                        opt("client", "Client organization using IT products, services or advice from vendors", "Организация-заказчик, которая использует ИТ-продукты, услуги или советы поставщиков", "ארגון לקוח שמשתמש במוצרי IT, בשירותים או בייעוץ של ספקים"),
                        opt("both", "Both", "И то и другое", "שניהם"),
                        OTHER,
                    ],
                ),
            ],
        },
        {
            "id": "situation",
            "title": t(
                "A recent AI-assisted work situation",
                "Недавняя рабочая ситуация с помощью ИИ",
                "מצב עבודה אחרון בסיוע בינה מלאכותית",
            ),
            "questions": [
                textq(
                    "q2_1", "2.1",
                    "Please describe a recent work situation where you used or received AI-generated or AI-assisted information. What were you trying to do?",
                    "Опишите недавнюю рабочую ситуацию, в которой вы использовали или получили информацию, созданную или подготовленную с помощью ИИ. Что вы пытались сделать?",
                    "תאר מצב עבודה מהזמן האחרון שבו השתמשת או קיבלת מידע שנוצר או הוכן בסיוע בינה מלאכותית. מה ניסית לעשות?",
                ),
                textq(
                    "q2_2", "2.2",
                    "What information or recommendation did the AI provide, and what did you understand or conclude from it?",
                    "Какую информацию или рекомендацию дал ИИ, и что вы из этого поняли или заключили?",
                    "איזה מידע או המלצה סיפקה הבינה המלאכותית, ומה הבנת או הסקת מזה?",
                ),
                choice(
                    "q2_3", "2.3", "multi",
                    "What did you do with the AI-provided information? Select every item that applies.",
                    "Что вы сделали с информацией от ИИ? Отметьте всё подходящее.",
                    "מה עשית עם המידע שסיפקה הבינה המלאכותית? סמן כל מה שמתאים.",
                    [
                        opt("as_provided", "Used it as provided", "Использовал как есть", "השתמשתי בו כפי שניתן"),
                        opt("part", "Used part of it", "Использовал часть", "השתמשתי בחלק ממנו"),
                        opt("changed", "Used it after making changes", "Использовал после изменений", "השתמשתי בו אחרי ששיניתי"),
                        opt("checked", "Checked it before using it", "Проверил перед использованием", "בדקתי לפני השימוש"),
                        opt("discussed", "Discussed or reviewed it with someone else", "Обсудил или проверил с кем-то ещё", "דנתי או בדקתי עם מישהו אחר"),
                        opt("passed", "Passed it to someone else", "Передал кому-то ещё", "העברתי למישהו אחר"),
                        opt("not_used", "Decided not to use it", "Решил не использовать", "החלטתי לא להשתמש"),
                        OTHER,
                    ],
                ),
                {
                    **choice(
                        "q2_3_knew", "2.3a", "single",
                        "If you passed it to someone else: did they know AI was involved?",
                        "Если вы передали это кому-то ещё: знал ли этот человек, что был задействован ИИ?",
                        "אם העברת את זה למישהו אחר: האם הוא ידע שבינה מלאכותית הייתה מעורבת?",
                        [
                            opt("yes", "Yes", "Да", "כן"),
                            opt("no", "No", "Нет", "לא"),
                            opt("unsure", "Not sure", "Не уверен", "לא בטוח"),
                            opt("na", "Not applicable", "Неприменимо", "לא רלוונטי"),
                            OTHER,
                        ],
                    ),
                    "showIf": {"question": "q2_3", "includes": "passed"},
                },
                textq(
                    "q2_4", "2.4",
                    "What was the result or outcome of the situation?",
                    "Каков был результат этой ситуации?",
                    "מה הייתה התוצאה של המצב?",
                ),
            ],
        },
        {
            "id": "assess",
            "title": t(
                "How you assessed the information",
                "Как вы оценивали информацию",
                "איך הערכת את המידע",
            ),
            "questions": [
                textq(
                    "q3_1", "3.1",
                    "What made you decide that the information was suitable, or not suitable, to use? If you checked or discussed it, how did you do that?",
                    "Что заставило вас решить, что информацию можно или нельзя использовать? Если вы проверяли или обсуждали её, как именно?",
                    "מה גרם לך להחליט שהמידע מתאים, או לא מתאים, לשימוש? אם בדקת או דנת בו, איך עשית את זה?",
                    probe=t(
                        "Optional interviewer probe if not raised: did the way the information was presented, such as its tone, level of detail or format, affect your confidence?",
                        "Дополнительный вопрос интервьюера, если участник сам не сказал: повлияли ли на вашу уверенность тон, подробность или формат подачи?",
                        "שאלת מראיין אם לא עלה מעצמו: האם אופן הצגת המידע, כמו הטון, רמת הפירוט או הפורמט, השפיע על הביטחון שלך?",
                    ),
                ),
                textq(
                    "q3_2", "3.2",
                    "Was anything unclear, missing, or open to a different understanding? Did you or anyone else consider another explanation or conclusion?",
                    "Было ли что-то неясным, недостающим или допускающим другое понимание? Рассматривали ли вы или кто-то ещё другое объяснение или вывод?",
                    "האם משהו היה לא ברור, חסר, או פתוח להבנה אחרת? האם אתה או מישהו אחר שקלתם הסבר או מסקנה אחרים?",
                ),
                textq(
                    "q3_3", "3.3",
                    "Did anything later cause you to change your understanding, decision, or action? If yes, what happened?",
                    "Заставило ли что-то позже изменить понимание, решение или действие? Если да, что произошло?",
                    "האם משהו בהמשך גרם לך לשנות את ההבנה, ההחלטה או הפעולה? אם כן, מה קרה?",
                ),
            ],
        },
        {
            "id": "wrong",
            "title": t(
                "A situation that went wrong or nearly went wrong",
                "Ситуация, которая пошла не так или почти пошла не так",
                "מצב שהשתבש או כמעט השתבש",
            ),
            "lead": t(
                "If you have no such example, skip these questions and continue.",
                "Если такого примера нет, пропустите эти вопросы и продолжайте.",
                "אם אין דוגמה כזו, דלגו על השאלות האלה והמשיכו.",
            ),
            "questions": [
                textq(
                    "q4_1", "4.1",
                    "Please think of a different situation, if you have one, where AI-assisted information led or nearly led to a problem, misunderstanding, or poor decision. What happened, and what was at stake?",
                    "Вспомните другую ситуацию, если она была, в которой информация с помощью ИИ привела или едва не привела к проблеме, недопониманию или неудачному решению. Что произошло и что было поставлено на карту?",
                    "חשוב על מצב אחר, אם היה, שבו מידע שנעזר בבינה מלאכותית הוביל או כמעט הוביל לבעיה, אי-הבנה או החלטה לא טובה. מה קרה, ומה עמד על כף המאזניים?",
                ),
                textq(
                    "q4_2", "4.2",
                    "Looking back, what do you think caused the problem: what the AI produced, how it was understood, how it was used or passed on, or something else? How was the problem noticed, and what happened afterwards?",
                    "Оглядываясь назад, что, по-вашему, вызвало проблему: то, что произвёл ИИ, то, как это поняли, то, как это использовали или передали, или что-то ещё? Как проблему заметили и что было потом?",
                    "במבט לאחור, מה לדעתך גרם לבעיה: מה שהבינה המלאכותית ייצרה, איך זה הובן, איך זה שימש או הועבר, או משהו אחר? איך הבחינו בבעיה, ומה קרה אחר כך?",
                    probe=t(
                        "Optional interviewer probes if not raised: time pressure, familiarity with the topic, missing context, how confident the output sounded, pressure from others, or unclear ownership.",
                        "Дополнительные вопросы интервьюера, если не прозвучало: нехватка времени, знакомство с темой, недостающий контекст, уверенный тон ответа, давление других людей или неясная ответственность.",
                        "שאלות מראיין אם לא עלו: לחץ זמן, היכרות עם הנושא, הקשר חסר, עד כמה הפלט נשמע בטוח, לחץ מאחרים, או בעלות לא ברורה.",
                    ),
                ),
            ],
        },
        {
            "id": "org",
            "title": t(
                "How AI-assisted information is handled in your organization",
                "Как в вашей организации обращаются с информацией при помощи ИИ",
                "איך בארגון מטפלים במידע שנעזר בבינה מלאכותית",
            ),
            "questions": [
                textq(
                    "q5_1", "5.1",
                    "Does your organization have any rules, guidance, checks, or approval requirements for using AI-assisted information? Who is responsible for the final decision?",
                    "Есть ли в вашей организации правила, рекомендации, проверки или требования согласования для использования информации с помощью ИИ? Кто отвечает за окончательное решение?",
                    "האם בארגון יש כללים, הנחיות, בדיקות או דרישות אישור לשימוש במידע שנעזר בבינה מלאכותית? מי אחראי להחלטה הסופית?",
                ),
                textq(
                    "q5_2", "5.2",
                    "If AI-assisted information causes or nearly causes a problem, how is it handled or learned from? What would most help improve the way it is handled?",
                    "Если информация с помощью ИИ вызывает или едва не вызывает проблему, как с этим поступают и какие выводы делают? Что больше всего помогло бы улучшить такое обращение?",
                    "אם מידע שנעזר בבינה מלאכותית גורם או כמעט גורם לבעיה, איך מטפלים בזה או לומדים מזה? מה הכי יעזור לשפר את הטיפול?",
                ),
            ],
        },
        {
            "id": "close",
            "title": t("Closing", "Завершение", "סיום"),
            "questions": [
                textq(
                    "c1", "C.1",
                    "Is there anything important that these questions did not cover, anything that was unclear, or anything you could not discuss because of confidentiality?",
                    "Есть ли что-то важное, чего эти вопросы не затронули, что-то неясное, или то, что вы не могли обсудить из-за конфиденциальности?",
                    "האם יש משהו חשוב שהשאלות האלה לא כיסו, משהו שלא היה ברור, או משהו שלא יכולת לדון בו בגלל סודיות?",
                ),
            ],
        },
    ],
}

path = Path(__file__).with_name("instrument.json")
path.write_text(json.dumps(instrument, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(path, "questions", sum(len(s["questions"]) for s in instrument["sections"]))
