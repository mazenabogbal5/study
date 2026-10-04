import json
import re

terms_raw = """
Pathology = علم الأمراض
Pathogenesis = الآلية الإمراضية (ميكانيزم حدوث المرض)
Morphologic changes = التغيرات الشكلية (المورفولوجية)
Gross changes = التغيرات العيانية (بالعين المجردة)
Microscopic changes = التغيرات المجهرية (تحت المجهر)
Complications = المضاعفات المرضية
Inflammation = الالتهاب
Immune-vascular response = استجابة مناعية وعائية
Living tissue = النسيج الحي
Injury = الإصابة / الأذى النسيجي
Infectious agents = العوامل المُعدية (كالبكتيريا والفيروسات)
Immunological causes = أسباب مناعية
Tissue necrosis = نخر الأنسجة (موت الأنسجة)
Chemical agents = عوامل كيميائية
Physical agents = عوامل فيزيائية
Nutritional causes = أسباب غذائية
Immune cells = الخلايا المناعية
Blood vessels = الأوعية الدموية
Chemical mediators = الوسطاء الكيميائية
Cardinal signs = العلامات الأساسية (الموضعية) للالتهاب
Redness = الاحمرار
Swelling = التورم
Pain = الألم
Loss of function = فقدان الوظيفة
Vasodilatation / Vasodilation = توسع الأوعية الدموية
Inflammatory exudate = الرشاحة الالتهابية
Edema fluid = سائل الوذمة
Toxins = السموم
Nerve ending irritation = تهيج النهايات العصبية
Vascular phenomena = الظواهر الوعائية
Transient vasoconstriction = انقباض وعائي مؤقت
Trauma = الصدمة / الخبطة الجسدية
Histamine = الهيستامين
Slowing of circulation (Stasis) = بطء الدورة الدموية (الركود الدموي)
Hemoconcentration = تركز الدم (زيادة لزوجته)
Endothelial cells / Endothelium = الخلايا البطانية (بطانة الأوعية الدموية)
Escape of plasma = تسرب / هروب البلازما
Leukocytes extravasation = خروج / تسرب خلايا الدم البيضاء
Diapedesis = الانسلال الخلوي عبر الأوعية
Chemo-attraction = الانجذاب الكيميائي
Margination = التهميش (التصاق الخلايا بجوانب الوعاء)
Cell Activation = تنشيط / تفعيل الخلايا
Pathogens = مسببات الأمراض
Interleukin-1 (IL-1) = إنترلوكين-1
Tumor Necrosis Factor alpha (TNF-α) = عامل نخر الورم ألفا
Selectins (E-selectin & P-selectin) = السليكتينات (بروتينات الالتصاق الوعائي)
Rolling = الدحرجة الخلوية
Carbohydrate ligands = ربيطات الكربوهيدرات
Adhesion = الالتصاق الخلوي
Integrins = الانتيجرينات (جزيئات الالتصاق المباشر)
Immobilization = تثبيت / شلل حركة الخلايا
Transmigration = الهجرة عبر الأوعية
Pseudopodia = الأقدام الكاذبة
Proteolytic digestion = الهضم الإنزيمي للبروتينات
Basement membrane = الغشاء القاعدي
PECAM-1 = جزيء التصاق الخلايا البطانية الوعائية-1
Neutrophils = الخلايا المتعادلة (العدلات)
Phagocytosis = البلعمة (الابتلاع الخلوي)
ROS (Reactive Oxygen Species) = أنواع الأكسجين التفاعلية / النشطة
Lysosomes = الجسيمات الحالة (الليزوسومات)
Dilution of toxins = تخفيف تركيز السموم
Fibrinogen = الفيبرينوجين (مولد الفيبرين)
Fibrin threads = خيوط الفيبرين
Localization of infection = تحجيم / توطين العدوى
Antibodies = الأجسام المضادة
Neutralization = التعادل / الإبطال (إبطال السموم)
Opsonization = الطهي / التطهية (تسهيل البلعمة)
Agglutination = التلازن / التجميع في خثرات
Antibody mediated cell cytotoxicity = السمية الخلوية المعتمدة على الأجسام المضادة
NK cells (Natural Killer cells) = الخلايا القاتلة الطبيعية
Complement system = النظام المتمم (المكمل المناعي)
Cytokines = السيتوكينات (ناقلات الإشارات المناعية)
Membrane Attack Complex (MAC) = معقد هجوم الغشاء
Cell lysis = تحلل وتفجر الخلايا
Anaphylatoxins (C3a, C5a) = التوكسينات التأقية / التأقانيات
Leukocyte chemoattractant = جاذب كيميائي لخلايا الدم البيضاء
Classical pathway = المسار الكلاسيكي (التقليدي)
Alternative pathway = المسار البديل
C3 convertase = إنزيم محول C3
Chemotaxis = الانجذاب الكيميائي
Phagocyte = الخلية البلعمية
Phagosome = الجسيم البلعمي (الفاجوسوم)
Phagolysosome = الجسيم الحال البلعمي (الفاجوليزوسوم)
Exocytosis = الإخراج الخلوي / طرح الفضلات
Acute inflammation = الالتهاب الحاد
Chronic inflammation = الالتهاب المزمن
Onset = بدء المرض / ظهور الأعراض
Duration = المدة الزمنية
Toxemia = تسمم الدم
Lymphocytes = الخلايا الليمفاوية
Plasma cells = الخلايا البلازمية
Giant cells = الخلايا العملاقة
Fibroblasts = الخلايا الليفية اليافعة
Angiogenesis = تخلق أوعية دموية جديدة
Endarteritis obliterans = التهاب بطانة الشرايين الساد
Eosinophil = الخلايا الحامضية (الإيوسينات)
Macrophage = الخلايا البلعمية الكبيرة (الماكروفاج)
Fever = الحمى (ارتفاع الحرارة)
Leukocytosis = زيادة عدد كرات الدم البيضاء
Suppurative inflammation = الالتهاب القيحي / الصديدي
Reticulo-endothelial system = الجهاز الشبكي البطاني
Kupffer cells = خلايا كوففر (في الكبد)
Cloudy swelling = التورم الغائم (الضمور المائي)
Cell death (Necrosis) = موت الخلايا (النخر)
Sepsis = إنتان الدم / تعفن الدم
Pyemia = تقيح الدم (وجود صديد في الدم)
Beneficial effects = الآثار المفيدة
Harmful effects = الآثار الضارة
Healing by fibrosis = التلائم بالتليف
Pressure atrophy = الضمور الضغطي
Hypersensitivity = فرط الحساسية
Serotonin = السيروتونين
Prostaglandins = البروستاغلاندينات
Leukotrienes (LTB4) = الليوكوترينات
Platelet activating factors (PAF) = عوامل تنشيط الصفائح الدموية
Nitric oxide (NO) = أكسيد النيتريك
Bradykinin = البراديكينين
Factor XII (Hageman factor) = العامل XII (عامل هاجمان)
"""

qa_raw = """
Q1: Define pathology?
English: The science of the disease study. It deals with 5 components of the disease: 1- Definition, 2- Causes, 3- Mechanisms (pathogenesis), 4- Morphologic changes (Gross and Microscopic), 5- Complications.
Arabic: (س: عرّف علم الأمراض؟ / ج: هو علم دراسة المرض. وبيتعامل مع 5 مكونات للمرض: 1- التعريف، 2- الأسباب، 3- الآلية الإمراضية "الميكانيزم"، 4- التغيرات الشكلية "بالعين والميكروسكوب"، 5- المضاعفات).

Q2: Define pathogenesis?
English: Pathogenesis refers to the mechanisms of the disease.
Arabic: (س: عرّف الآلية الإمراضية؟ / ج: الآلية الإمراضية تشير إلى آليات أو ميكانيزمات حدوث المرض).

Q3: Define inflammation?
English: It is a protective immune-vascular response. It is the reaction of living tissue against injury.
Arabic: (س: عرّف الالتهاب؟ / ج: هو استجابة وقائية مناعية ووعائية. وهو رد فعل الأنسجة الحية ضد الإصابة).

Q4: Mention the causes of inflammation?
English: 1- Infectious agents, 2- Immunological, 3- Tissue necrosis, 4- Nutritional, 5- Chemical and physical agents.
Arabic: (س: اذكر أسباب الالتهاب؟ / ج: 1- عوامل مُعدية، 2- مناعية، 3- نخر الأنسجة، 4- غذائية، 5- عوامل كيميائية وفيزيائية).

Q5: What are the main components of inflammation?
English: 1- Cause, 2- Immune Cells, 3- Blood vessels, 4- Chemical mediators.
Arabic: (س: ما هي المكونات الأساسية للالتهاب؟ / ج: 1- المُسبب، 2- الخلايا المناعية، 3- الأوعية الدموية، 4- الوسطاء الكيميائية).

Q6: What is the purpose of inflammation?
English: 1- Elimination of the cause, 2- Clear necrotic cells, 3- Initiate repair.
Arabic: (س: ما هو الغرض من الالتهاب؟ / ج: 1- القضاء على المُسبب، 2- التخلص من الخلايا الميتة، 3- بدء عملية الإصلاح).

Q7: Summarize the events of inflammation?
English: 1- Injury: Tissue damage or infection occurs. 2- Chemical mediators: Release of mediators like Histamine from damaged cells. 3- Vasodilatation: Blood vessels widen to bring more blood. 4- Inflammatory exudate formation: Escape of plasma and blood cells (neutrophils) from blood vessels to the tissue. 5- Chemotaxis & phagocytosis: WBCs move toward the microbes to kill them.
Arabic: (س: لخص أحداث الالتهاب؟ / ج: 1- الإصابة: يحدث تلف للنسيج أو عدوى. 2- الوسطاء الكيميائية: إفراز وسائط زي الهيستامين من الخلايا المتضررة. 3- توسع الأوعية: الأوعية بتوسع عشان تجيب دم أكتر. 4- تكوين الرشاحة الالتهابية: خروج البلازما وخلايا الدم "المتعادلات" للنسيج. 5- الانجذاب والبلعمة: كرات الدم البيضاء بتتحرك تجاه الميكروبات لقتلها).

Q8: What are the main components of normal blood?
English: 1- Plasma (water + protein), 2- Platelets, 3- Red blood cells, 4- White blood cells.
Arabic: (س: ما هي المكونات الأساسية للدم الطبيعي؟ / ج: 1- بلازما "ماء وبروتين"، 2- صفائح دموية، 3- كرات دم حمراء، 4- كرات دم بيضاء).

Q9: What is the inflammatory exudate formed of?
English: It is a fluid formed of plasma and blood cells (especially neutrophils). It comes out of the blood vessels to do specific immune functions.
Arabic: (س: مما تتكون الرشاحة الالتهابية؟ / ج: هي سائل يتكون من البلازما وخلايا الدم "خصوصاً المتعادلة". تخرج من الأوعية الدموية للقيام بوظائف مناعية محددة).

Q10: What are Neutrophils and what is their function in inflammation?
English: Neutrophils are a type of white blood cells. Their main function is phagocytosis and killing the microbe by ROS and Lysosomes.
Arabic: (س: ما هي الخلايا المتعادلة وما وظيفتها في الالتهاب؟ / ج: هي نوع من خلايا الدم البيضاء. وظيفتها الأساسية البلعمة وقتل الميكروب بواسطة مركبات الأكسجين النشطة والجسيمات الحالة).

Q11: Explain the role of Fibrinogen during inflammation?
English: Fibrinogen is normally an inactive protein dissolved in plasma. When it escapes into the tissue during inflammation, it becomes active and forms a network of fibrin threads. This network has two main roles: 1- Localization of infection, 2- Facilitates the movement of leucocytes.
Arabic: (س: اشرح دور الفيبرينوجين أثناء الالتهاب؟ / ج: هو عادة بروتين خامل ذائب في البلازما. ولما بيخرج للنسيج أثناء الالتهاب، بيصبح نشط ويُكوّن شبكة من خيوط الفيبرين. الشبكة دي لها دوران: 1- تحجيم العدوى، 2- تسهيل حركة كرات الدم البيضاء).

Q12: What is the role of Reactive Oxygen Species (ROS) during inflammation?
English: They are toxic oxygen molecules produced by white blood cells (especially neutrophils) to kill the engulfed microbes.
Arabic: (س: ما هو دور مركبات الأكسجين النشطة أثناء الالتهاب؟ / ج: هي جزيئات أكسجين سامة تنتجها خلايا الدم البيضاء لقتل الميكروبات التي تم ابتلاعها).

Q13: What are Lysosomes and what is their function in phagocytosis?
English: They are cellular sacs containing strong digestive enzymes, used by white blood cells to digest and break down the killed bacteria.
Arabic: (س: ما هي الجسيمات الحالة وما وظيفتها في البلعمة؟ / ج: هي أكياس خلوية تحتوي على إنزيمات هاضمة قوية، تستخدمها خلايا الدم البيضاء لهضم وتكسير البكتيريا المقتولة).

Q14: How is the microbe eliminated by neutrophils (WBCs)?
English: The process happens in 3 main steps: 1- Phagocytosis: Engulfing the microbe into the cell. 2- Killing: Using Reactive Oxygen Species (ROS) to kill the microbe. 3- Digestion: Using Lysosomes enzymes to digest and break down the killed microbe.
Arabic: (س: كيف يتم القضاء على الميكروب بواسطة المتعادلات؟ / ج: العملية تحدث في 3 خطوات: 1- البلعمة: ابتلاع الميكروب داخل الخلية. 2- القتل: استخدام مركبات الأكسجين النشطة لقتله. 3- الهضم: استخدام إنزيمات الجسيمات الحالة لهضم وتكسير الميكروب المقتول).

Q15: What are the cardinal (local) signs of inflammation and what are their causes?
English: The local signs are five: Redness (due to vasodilatation), Swelling (due to inflammatory fluid exudate), Pain (due to irritation of nerve endings by toxins and chemical mediators or compression), and Loss of function.
Arabic: (س: ما هي العلامات الأساسية (الموضعية) للالتهاب وما هي أسبابها؟ / ج: العلامات الموضعية خمسة: 1. الاحمرار: بسبب توسع الأوعية الدموية. 2. التورم: بسبب سائل الرشاحة الالتهابية. 3. الألم: بسبب تهيج النهايات العصبية بالسموم أو ضغط السائل. 4. فقدان الوظيفة).

Q16: Summarize the detailed steps of Vascular phenomena during acute inflammation?
English: 1- Transient vasoconstriction: Happens by direct action of toxins or trauma on blood vessels (reflex mechanism). 2- Vasodilatation: Caused by Histamine release. 3- Slowing of circulation (stasis): Occurs due to vasodilatation, hemoconcentration, and endothelial swelling. 4- Escape of plasma: Plasma moves from inside to outside blood vessels to form the fluid part of inflammatory exudate. 5- Leukocytes extravasation: WBCs exit through intact vessel walls via diapedesis.
Arabic: (س: لخص الخطوات التفصيلية للظواهر الوعائية أثناء الالتهاب الحاد؟ / ج: 1- انقباض وعائي مؤقت: رد فعل سريع للسموم أو الخبطة. 2- توسع الأوعية: بسبب الهيستامين. 3- بطء الدورة الدموية (الركود): بسبب التوسع، تركز الدم، وتورم بطانة الوعاء. 4- هروب البلازما: لتكوين الرشاحة الالتهابية. 5- خروج كرات الدم البيضاء: بالانسلال عبر جدران الأوعية).

Q17: What are the three main causes of slowing of circulation (stasis) during vascular phenomena?
English: Stasis occurs due to three reasons: 1- Vasodilatation. 2- Hemoconcentration (loss of fluid making blood thicker). 3- Swelling of endothelial cells lining the blood vessels.
Arabic: (س: ما هي الأسباب الثلاثة لبطء الدورة الدموية (الركود) أثناء الظواهر الوعائية؟ / ج: الركود بيحصل لـ 3 أسباب: 1- توسع الأوعية الدموية. 2- تركز الدم (بسبب خروج السوائل وزيادة لزوجة الدم). 3- تورم الخلايا البطانية المبطنة للأوعية الدموية).

Q18: Explain the detailed mechanisms and steps of Leukocyte extravasation?
English: Leukocyte extravasation occurs in 4 main steps: 1- Chemo-attraction, margination, and activation: Recognition of pathogens; cytokines (IL-1, TNF-α) stimulate endothelial cells to express E and P selectins. 2- Rolling: Carbohydrate ligands on leukocyte surfaces bind loosely to selectins. 3- Adhesion: Integrin molecules on leukocytes bind tightly to receptors on endothelial cells, immobilizing leukocytes. 4- Transmigration (Diapedesis): Leukocytes extend pseudopodia, pass through gaps between endothelial cells, and use proteolytic digestion to break the basement membrane.
Arabic: (س: اشرح آليات وخطوات خروج كرات الدم البيضاء من الأوعية الدموية بالتفصيل؟ / ج: 1- الانجذاب والتهميش والتنشيط: التعرف على الميكروب، وإنترلوكين-1 وعامل نخر الورم يخلو الخلايا البطانية تفرز السليكتينات. 2- الدحرجة: كربوهيدرات سطح كرات الدم بترتبط بالسليكتينات. 3- الالتصاق: جزيئات الانتيجرين ترتبط بصلابة بمستقبلات خلايا الوعاء فتثبت الخلية. 4- العبور (الانسلال): مد أقدام كاذبة والعبور بين الفتحات وهضم الغشاء القاعدي).

Q19: What are Selectins and Integrins, and what are their specific roles in leukocyte extravasation?
English: Selectins (E & P selectins): Endothelial adhesion molecules that bind carbohydrate ligands on leukocytes to mediate loose attachment and rolling. Integrins: Leukocyte surface molecules that bind tightly to receptors on endothelial cells to cause firm adhesion and immobilization.
Arabic: (س: ما هي السليكتينات والانتيجرينات وما دور كل منهما في خروج كرات الدم البيضاء؟ / ج: - السليكتينات: جزيئات التصاق تفرزها الخلايا البطانية للربط الكربوهيدراتي الخفيف والتسبب في الدحرجة. - الانتيجرينات: جزيئات على سطح كرات الدم البيضاء ترتبط بقوة بمستقبلات الوعاء لتثبيت الخلية).

Q20: What is Inflammatory Exudate and how is it formed?
English: It is an extravascular fluid formed of plasma and blood cells (especially neutrophils). It escapes out of blood vessels into tissue to perform specific immune functions.
Arabic: (س: ما هي الرشاحة الالتهابية وكيف تتكون؟ / ج: هي سائل يتكون من البلازما وخلايا الدم "خصوصاً المتعادلة"، يخرج من الأوعية الدموية للنسيج للقيام بوظائف مناعية محددة).

Q21: What are the main functions of the fluid part (Plasma) of inflammatory exudate?
English: 1- Dilution of toxins. 2- Fibrinogen conversion: Forms a network of fibrin threads causing localization of infection and facilitating leukocyte movement. 3- Contains plasma antibodies and complement proteins.
Arabic: (س: ما هي الوظائف الأساسية للجزء السائل (البلازما) في الرشاحة الالتهابية؟ / ج: 1- تخفيف تركيز السموم. 2- الفيبرينوجين يعمل شبكة خيوط تحجم العدوى وتسهل حركة الخلايا. 3- تحتوي على الأجسام المضادة والمتممات).

Q22: What are the 4 main functions of Antibodies in the inflammatory exudate?
English: 1- Neutralization: Block antigen receptors and toxins. 2- Opsonization: Coat the microorganism to facilitate phagocytosis. 3- Agglutination: Clumping microorganisms together to prevent spread. 4- Antibody-mediated cell cytotoxicity: Activate Natural Killer (NK) cells.
Arabic: (س: ما هي الوظائف الأربعة للأجسام المضادة في الرشاحة الالتهابية؟ / ج: 1- التعادل (الإبطال): غلق مستقبلات المستضد والسموم. 2- الطهي: تغليف الميكروب لتسهيل بلعمته. 3- التلازن (التجميع): تجميع الميكروبات لمنع انتشارها. 4- السمية الخلوية المعتمدة على الأجسام المضادة: تحفيز الخلايا القاتلة الطبيعية).

Q23: Define the Complement system, its origin, and how it is activated?
English: The complement system consists of small plasma proteins produced in the liver and circulating in inactive form. It is activated by antigen-antibody complexes or bacterial products.
Arabic: (س: عرّف النظام المتمم (المكمل المناعي)، وأين يتكون، وكيف يتنشط؟ / ج: يتكون من بروتينات صغيرة تفرزها الكبد وتدور في الدم بصورة خاملة. يتنشط بمعقدات المستضد والجسم المضاد أو منتجات البكتيريا).

Q24: What are the 3 primary functions of the Complement system in inflammation?
English: 1- Cell lysis: C5b binds to C6-C9 forming Membrane Attack Complex (MAC), forming holes in cell membranes causing cell lysis. 2- Inflammation promotion: C3a and C5a (anaphylatoxins) stimulate histamine release; C5a is a strong chemoattractant. 3- Opsonization: C3b binds to microbes to promote phagocytosis.
Arabic: (س: ما هي الوظائف الثلاث الرئيسية للنظام المتمم في الالتهاب؟ / ج: 1- تحلل الخلايا: (C5b) بيرتبط بـ (C6) إلى (C9) لتكوين معقد هجوم الغشاء (MAC) وتفجير الخلية. 2- تحفيز الالتهاب: (C3a) و (C5a) بيحفزوا إفراز الهيستامين، و (C5a) جاذب كيميائي قوي. 3- الطهي: (C3b) بيرتبط بالميكروب ويسهل بلعمته).

Q25: Explain the Complement Cascade pathways and Membrane Attack Complex (MAC) formation?
English: Activation functions via Classical pathway (C1 binding IgG) or Alternative pathway (bacterial surfaces). Both form C3 convertase, leading to C3 hydrolysis into C3a and C3b. C3b cleaves C5 into C5a and C5b. C5b, C6, C7, C8, and C9 aggregate to form the cylindrical Membrane Attack Complex (MAC), causing target cells to swell and burst.
Arabic: (س: اشرح شلال تنشيط المتممات وكيف يتكون معقد هجوم الغشاء (MAC)؟ / ج: يتم التنشيط عبر المسار الكلاسيكي أو البديل لتكوين إنزيم محول (C3)، ثم تحلل (C3) إلى (C3a) و (C3b). يكسر (C3b) بروتين (C5) إلى (C5a) و (C5b). يتجمع (C5b) مع (C6) و (C7) و (C8) و (C9) لتكوين معقد هجوم الغشاء الأسطواني (MAC) فتتفجر الخلية).

Q26: Define Chemotaxis and list the factors that act as chemoattractants?
English: Chemotaxis is the directed movement of white blood cells toward microbes or damaged sites. Chemoattractants include: 1- Bacterial toxins, 2- Complement components (especially C5a), 3- Factors released from necrotic tissue.
Arabic: (س: عرّف الانجذاب الكيميائي واذكر أهم العوامل الجاذبة؟ / ج: هو حركة كرات الدم البيضاء الموجهة نحو الميكروبات أو الأنسجة التالفة. والعوامل الجاذبة هي: سموم البكتيريا، مكونات المتمم (C5a)، ومواد الأنسجة الميتة).

Q27: Define Phagocytosis, its main function, and factors facilitating it?
English: Phagocytosis is the engulfing of foreign bodies (bacteria, debris) by neutrophils and macrophages to clean the area for repair. Factors helping: opsonins, complement, fibrin network, mild fever.
Arabic: (س: عرّف البلعمة، وما وظيفتها، وما العوامل التي تساعد عليها؟ / ج: ابتلاع الأجسام الغريبة بواسطة خلايا بلعمية لتنظيف منطقة الالتهاب تمهيداً للإصلاح. العوامل المساعدة: الطاهيات، المتممات، شبكة الفيبرين، والحمى الخفيفة).

Q28: What are the detailed 8 steps of Phagocytosis?
English: 1- Chemotaxis, 2- Adherence of microbe to phagocytes, 3- Ingestion, 4- Phagosome formation, 5- Fusion with lysosome to form Phagolysosome, 6- Digestion by enzymes and ROS, 7- Residual body formation, 8- Discharge of wastes (Exocytosis).
Arabic: (س: ما هي الخطوات الثمانية التفصيلية لعملية البلعمة؟ / ج: 1- الانجذاب، 2- الالتصاق، 3- الابتلاع، 4- الفاجوسوم، 5- الاندماج لتكوين الفاجوليزوسوم، 6- الهضم، 7- الجسم المتبقي، 8- الإخراج الخلوي).

Q29: Compare between Acute and Chronic inflammation based on all parameters?
English: Onset: Acute is Rapid; Chronic is Gradual. Duration: Acute lasts Few days; Chronic lasts Months/years. Cardinal signs: Present in acute; Absent in chronic. Toxemia: Acute in acute; Chronic in chronic. Microscopic Cells: Acute has Neutrophils and macrophages; Chronic has Macrophages, lymphocytes, plasma cells, giant cells, and fibroblasts. Edema fluid: Present in acute; Absent in chronic. Blood vessels: Acute has numerous, thin-walled, dilated vessels filled with blood; Chronic has less numerous, thick-walled vessels showing angiogenesis or endarteritis obliterans.
Arabic: (س: قارن بين الالتهاب الحاد والالتهاب المزمن؟ / ج: - البدء: الحاد سريع، المزمن تدريجي. - المدة: الحاد أيام، المزمن شهور/سنين. - العلامات الموضعية: موجودة بالحاد، غائبة بالمزمن. - التسمم: حاد في الحاد، مزمن بالمزمن. - الخلايا: الحاد فيه متعادلات وماكروفاج، المزمن فيه لمفاوية وبلازمية وخلايا عملاقة وألياف. - السائل: موجود بالحاد، غائب بالمزمن. - الأوعية: الحاد فيه أوعية رقيقة وواسعة، المزمن أوعية سميكة بها نمو جديد أو انسداد الشرايين).

Q30: Mention the specific biological role of each inflammatory cell type?
English: 1- Neutrophil: Active in suppurative inflammation; produces proteolytic enzymes and ROS. 2- Eosinophil: Dominant in parasitic inflammation and allergy. 3- Lymphocyte: Dominant in chronic and viral inflammation. 4- Fibroblast: Active in chronic inflammation; produces collagen for tissue repair. 5- Macrophage: Active in phagocytosis and clearing debris. 6- Giant cell: Engulfs large particles in chronic inflammation.
Arabic: (س: اذكر الدور البيولوجي المحدد لكل خلية التهابية؟ / ج: 1- المتعادلة: نشطة في الالتهاب القيحي وتفرز إنزيمات محللة. 2- الحامضية: في العدوى الطفيلية والحساسية. 3- الليمفاوية: في الالتهاب المزمن والفيروسي. 4- الليفية: تنتج الكولاجين لإصلاح الأنسجة. 5- الماكروفاج: بلعمة وتنظيف الحطام. 6- الخلية العملاقة: لابتلاع الأجسام الكبيرة).

Q31: What are the systemic biological changes associated with inflammation?
English: 1- Fever, 2- Leukocytosis, 3- Hyperplasia of the reticulo-endothelial system, 4- Reversible changes (cloudy swelling, fat accumulation), 5- Cell death (necrosis), 6- Toxemia, sepsis, and pyemia.
Arabic: (س: ما هي التغيرات البيولوجية العامة المصاحبة للالتهاب؟ / ج: 1- الحمى، 2- زيادة كرات الدم البيضاء، 3- فرط تنسج الجهاز الشبكي البطاني، 4- تغيرات عكسية بالخلايا "تغيم مائي أو دهون"، 5- موت الخلايا، 6- تسمم وتعفن الدم ووجود صديد بالدم).

Q32: What is Hyperplasia of the Reticulo-Endothelial system during inflammation?
English: It is the hyperplasia (increased cell number) of phagocytic tissue cells, such as Kupffer cells of the liver and tissue histiocytes, to enhance phagocytosis and clear toxins.
Arabic: (س: ما هو فرط تنسج الجهاز الشبكي البطاني أثناء الالتهاب؟ / ج: هو زيادة عدد خلايا البلعميات النسيجية مثل خلايا كوففر بالكبد لزيادة قدرة البلعمة وتنقية السموم).

Q33: Compare between the beneficial and harmful effects of inflammation?
English: Beneficial effects: Dilution of toxins, phagocytosis, localization by fibrin, and induction of immunity. Harmful effects: Swelling causing obstructions and loss of function; Healing by fibrosis causing narrowing, pressure atrophy, and organ dysfunction; Hypersensitivity.
Arabic: (س: قارن بين الآثار المفيدة والآثار الضارة للالتهاب؟ / ج: - المفيدة: تخفيف السموم، البلعمة، تحجيم العدوى، وتنشيط المناعة. - الضارة: تورم يسبب انسداد المجاري وفقدان الوظيفة، تليف يسبب تضيق وضمور الأعضاء، وفرط الحساسية).

Q34: Define Chemical Mediators and mention their source and stimulus for release?
English: Chemical mediators are molecules derived from cells or plasma that direct and regulate vascular and cellular events of inflammation. Produced in response to microbial products or necrotic tissues.
Arabic: (س: عرف الوسطاء الكيميائية واذكر مصدرها وما يثير إفرازها؟ / ج: هي جزيئات تنشأ من الخلايا أو البلازما وتنظم أحداث الالتهاب الوعائية والخلوية. تُفرز كـ رد فعل للميكروبات أو الأنسجة الميتة).

Q35: Mention the Preformed Cellular Chemical Mediators, their sources, and actions?
English: 1- Histamine: Source: Mast cells, Basophils, Platelets. Actions: Vascular leakage (Yes), Chemotaxis (No). 2- Serotonin: Source: Platelets. Actions: Vascular leakage (Yes), Chemotaxis (No). 3- Lysosomal Enzymes: Source: Neutrophils, Macrophages. Actions: Tissue digestion.
Arabic: (س: اذكر الوسطاء الكيميائية الخلوية المخزنة مسبقاً ومصادرها وتأثيراتها؟ / ج: 1- الهيستامين: من الخلايا الصارية والقاعدية والصفائح (تسريب وعائي). 2- السيروتونين: من الصفائح (تسريب وعائي). 3- إنزيمات الجسيمات الحالة: من كرات الدم والماكروفاج (هضم الأنسجة)).

Q36: Mention Newly Synthesized Cellular Chemical Mediators, their sources, and actions?
English: 1- Prostaglandins: Source: Leukocytes, platelets, endothelial cells (Vasodilation, pain, fever). 2- Leukotrienes: Source: Leukocytes, mast cells (Vascular leakage, Chemotaxis LTB4, bronchoconstriction). 3- PAF: Source: Leukocytes, endothelial cells (Vascular leakage, Chemotaxis, bronchoconstriction). 4- ROS: Source: Leukocytes (Vascular leakage, tissue damage). 5- Nitric Oxide: Source: Macrophages, endothelial cells (Vasodilation, cytotoxicity). 6- Cytokines (IL-1, IL-8, TNF): Source: Lymphocytes, macrophages, endothelial cells (Chemotaxis, leukocyte activation, fever).
Arabic: (س: اذكر الوسطاء الكيميائية الخلوية المصنعة حديثاً ومصادرها؟ / ج: 1- البروستاغلاندينات (توسع أوعية، ألم، حمى). 2- الليوكوترينات (تسريب وعائي، انجذاب LTB4). 3- PAF (تسريب وعائي وانجذاب وانقباض شعب). 4- ROS (تسريب وعائي وتلف أنسجة). 5- أكسيد النيتريك (توسع أوعية وسمية). 6- السيتوكينات (انجذاب وتنشيط الخلايا وحمى)).

Q37: Mention Plasma-Derived Chemical Mediators and their mechanisms?
English: 1- Factor XII (Hageman factor) activation: Kinin system (Bradykinin): Vascular leakage (Yes), Pain. Coagulation/Fibrinolysis system: Stabilize platelet plug / Lyse fibrin plug. 2- Complement activation: C3a (Vascular leakage & Chemotaxis), C3b (Opsonization), C5a (Chemotaxis, adhesion, activation), C5b-9 (MAC - Cell lysis).
Arabic: (س: اذكر الوسطاء الكيميائية المشتقة من البلازما؟ / ج: 1- تنشيط العامل XII: نظام الكينين (البراديكينين للألم والتسريب)، نظام التجلط والتحلل. 2- تنشيط المتممات: (C3a) تسريب وانجذاب، (C3b) طهي، (C5a) انجذاب والتصاق، و (C5b-9) هو معقد هجوم الغشاء (MAC) لتفجير الخلية).

Q38: Solve the Formative Exam questions listed at the end of the file?
English: 1- Mention three criteria of inflammatory exudate: Extravascular fluid formed of plasma and neutrophils; contains fibrinogen/proteins; escapes outside vessels to do immune functions. 2- What are selectins and integrin: Selectins are endothelial molecules causing rolling; Integrins are leukocyte molecules causing firm adhesion. 3- What is opsonization: Coating of microorganisms with opsonins (antibodies or C3b) to promote phagocytosis. 4- List three functions of complement: Cell lysis (MAC C5b-9), Inflammation promotion (C3a/C5a), Opsonization (C3b). 5- Define chemical mediators: Molecules derived from cells or plasma that direct and regulate vascular and cellular events of inflammation.
Arabic: (س: أجب عن أسئلة الامتحان التقييمي المذكور في نهاية الملف؟ / ج: 1- ثلاثة خصائص للرشاحة: سائل به بلازما وخلايا متعادلة، يحتوي على بروتينات وفيبرينوجين، ويخرج للقيام بوظائف مناعية. 2- السليكتينات والانتيجرينات: السليكتينات للدحرجة، والانتيجرينات للالتصاق الصلب. 3- الطهي: تغليف الميكروب لتسهيل بلعمته. 4- ثلاثة وظائف للمتمم: تحلل الخلايا، تحفيز الالتهاب، والطهي. 5- الوسطاء الكيميائية: جزيئات خلوية أو بلازمية تنظم أحداث الالتهاب الوعائية والخلوية).

Q39: Summarize the complete storyline and timeline of acute inflammation from initial injury until final pathogen clearance?
English: 1- Injury: Tissue damage occurs, releasing microbial products and necrotic cell factors. 2- Release of Chemical Mediators: Injured cells release Histamine, Bradykinin, and Cytokines. 3- Vascular Response: Brief transient vasoconstriction, followed by vasodilatation, increased permeability, slowing of circulation (stasis), and escape of plasma to form inflammatory exudate. 4- Leukocyte Recruitment: Neutrophils undergo margination, rolling via Selectins, firm adhesion via Integrins, and transmigration (diapedesis) using PECAM-1 and proteolytic enzymes to cross basement membrane. 5- Chemotaxis: Neutrophils travel along chemoattractant gradients (C5a, bacterial toxins) toward microbes. 6- Phagocytosis & Destruction: Neutrophils bind to opsonized bacteria (coated with C3b/Antibodies), engulf them into phagosomes, fuse with lysosomes to form phagolysosomes, and destroy/digest them using ROS and lysosomal proteases.
Arabic: (س: لخص القصة الكاملة وحدوث الالتهاب الحاد منذ البداية لحظة الإصابة وحتى القضاء التام على الميكروب؟ / ج: 1- حدوث الإصابة: تلف النسيج وخروج مواد الميكروب وخلايا ميتة. 2- إفراز الوسطاء: إفراز الهيستامين والسيتوكينات. 3- الاستجابة الوعائية: انقباض خاطف، ثم توسع الأوعية، ركود الدم، وخروج البلازما لتكوين الرشاحة. 4- خروج كرات الدم البيضاء: تهميش الخلايا المتعادلة، دحرجتها بالسليكتينات، التصاقها القوي بالانتيجرينات، وعبورها بالانسلال والإنزيمات عبر الغشاء القاعدي. 5- الانجذاب الكيميائي: التحرك نحو الميكروب بتأثير (C5a) وسموم البكتيريا. 6- البلعمة والتدمير: التصاق المتعادلات بالميكروب المطهى، ابتلاعه داخل فاجوسوم، اندماجه مع الليزوسوم، وقتله وهضمه بمركبات الأكسجين النشطة والإنزيمات الهاضمة).
"""

exam_raw = """
Question 1: Mention three criteria of inflammatory exudate?
English: 1- It is an extravascular fluid formed of plasma and blood cells (especially neutrophils). 2- It contains high concentration of proteins and fibrinogen which forms fibrin network. 3- It escapes out of the blood vessels into tissue to perform specific immune functions (dilution of toxins, opsonization, localization of infection).
Arabic: (س1: اذكر ثلاثة خصائص للرشاحة الالتهابية؟ / ج1: 1- سائل خارج الأوعية الدموية بيتكون من البلازما وخلايا الدم "خصوصاً المتعادلة". 2- يحتوي على تركيز عالٍ من البروتينات والفيبرينوجين اللي بيكوّن شبكة الفيبرين. 3- بيخرج من الأوعية الدموية للنسيج عشان يقوم بوظائف مناعية محددة مثل تخفيف السموم والطهي وتحجيم العدوى).

Question 2: What are selectins and integrin?
English: - Selectins (E-selectin & P-selectin): Adhesion molecules expressed on endothelial cells that bind carbohydrate ligands on leukocytes to cause loose attachment and "Rolling". - Integrins: Adhesion molecules expressed on leukocyte surfaces that bind tightly to receptors on endothelial cells causing firm "Adhesion" and immobilization of leukocytes.
Arabic: (س2: ما هي السليكتينات والانتيجرينات؟ / ج2: - السليكتينات: جزيئات التصاق بتفرزها الخلايا البطانية للوعاء الدموي، بترتبط بـ كربوهيدرات سطح كرات الدم البيضاء فتسبب الارتباط الضعيف والدحرجة. - الانتيجرينات: جزيئات التصاق على سطح كرات الدم البيضاء، بترتبط بقوة بمستقبلات الخلايا البطانية فتسبب الالتصاق الصلب وتثبيت الخلية تماماً).

Question 3: What is opsonization?
English: It is the process of coating the microorganisms or pathogens with specific plasma molecules called "Opsonins" (such as antibodies IgG or complement component C3b) to facilitate their recognition and engulfment by phagocytic cells (neutrophils and macrophages).
Arabic: (س3: ما هي عملية الطهي (Opsonization)؟ / ج3: هي عملية تغليف الميكروبات أو مسببات الأمراض بمواد بلازمية محددة تسمى "الطاهيات" مثل الأجسام المضادة (IgG) أو مركب المتمم (C3b) لتسهيل التعرف عليها وابتلاعها بواسطة الخلايا البلعمية).

Question 4: List three functions of complement?
English: 1- Cell lysis: Formation of Membrane Attack Complex (MAC / C5b-9) which creates holes in target cell membrane causing cell lysis. 2- Inflammation promotion: C3a and C5a (anaphylatoxins) stimulate histamine release, and C5a acts as a strong leukocyte chemoattractant. 3- Opsonization: C3b binds to microbial surface receptors to promote phagocytosis by neutrophils and macrophages.
Arabic: (س4: اذكر ثلاث وظائف للنظام المتمم (المكمل المناعي)؟ / ج4: 1- تحلل الخلايا: تكوين معقد هجوم الغشاء (MAC / C5b-9) اللي بيعمل ثقوب في غشاء الخلية وتفجيرها. 2- تحفيز الالتهاب: (C3a) و (C5a) بيحفزوا إفراز الهيستامين، و (C5a) جاذب كيميائي قوي لخلايا الدم البيضاء. 3- الطهي: (C3b) بيرتبط بمستقبلات سطح الميكروب ويسهل بلعمته).

Question 5: Define chemical mediators?
English: They are biologically active molecules derived either from cells (preformed or newly synthesized) or from plasma (liver-derived) that direct, initiate, and regulate the vascular and cellular events of inflammation in response to microbial products or necrotic tissue factors.
Arabic: (س5: عرّف الوسطاء الكيميائية؟ / ج5: هي جزيئات نشطة بيولوجياً بتنشأ إما من الخلايا "مخزنة أو مصنعة حديثاً" أو من البلازما "من الكبد"، وتقوم بتوجيه وبدء وتنظيم جميع الأحداث الوعائية والخلوية للالتهاب كـ رد فعل لمنتجات الميكروبات أو مواد الأنسجة الميتة).
"""

# Parse Terms
terms = []
for line in terms_raw.strip().split("\n"):
    line = line.strip()
    if not line or "=" not in line:
        continue
    parts = line.split("=", 1)
    en = parts[0].strip()
    ar = parts[1].strip()
    terms.append({"id": len(terms) + 1, "en": en, "ar": ar})

print(f"Parsed {len(terms)} terms.")

# Parse Q&A
qa_items = []
qa_blocks = re.split(r'\n(?=Q\d+:)', qa_raw.strip())
for block in qa_blocks:
    block = block.strip()
    if not block:
        continue
    m_q = re.search(r'Q(\d+):\s*(.+?)(?=\nEnglish:|$)', block, re.DOTALL)
    m_en = re.search(r'English:\s*(.+?)(?=\nArabic:|$)', block, re.DOTALL)
    m_ar = re.search(r'Arabic:\s*(.+)$', block, re.DOTALL)
    if m_q and m_en and m_ar:
        q_num = int(m_q.group(1))
        q_text = m_q.group(2).strip()
        en_ans = m_en.group(1).strip()
        ar_ans = m_ar.group(1).strip()
        qa_items.append({
            "id": q_num,
            "q": q_text,
            "en": en_ans,
            "ar": ar_ans
        })

print(f"Parsed {len(qa_items)} Q&A items.")

# Parse Exam
exam_items = []
exam_blocks = re.split(r'\n(?=Question\s*\d+:)', exam_raw.strip())
for block in exam_blocks:
    block = block.strip()
    if not block:
        continue
    m_q = re.search(r'Question\s*(\d+):\s*(.+?)(?=\nEnglish:|$)', block, re.DOTALL)
    m_en = re.search(r'English:\s*(.+?)(?=\nArabic:|$)', block, re.DOTALL)
    m_ar = re.search(r'Arabic:\s*(.+)$', block, re.DOTALL)
    if m_q and m_en and m_ar:
        q_num = int(m_q.group(1))
        q_text = m_q.group(2).strip()
        en_ans = m_en.group(1).strip()
        ar_ans = m_ar.group(1).strip()
        exam_items.append({
            "id": q_num,
            "q": q_text,
            "en": en_ans,
            "ar": ar_ans
        })

print(f"Parsed {len(exam_items)} Exam items.")

with open("c:/STUDY/data.json", "w", encoding="utf-8") as f:
    json.dump({
        "terms": terms,
        "qa": qa_items,
        "exam": exam_items
    }, f, ensure_ascii=False, indent=2)

print("Saved data.json successfully.")


