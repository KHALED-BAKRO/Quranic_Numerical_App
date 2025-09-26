import json
from enum import Enum

# ====== 1. تعريف النماذج المنهجية (Enums & Class) ======

class PhenomenonType(Enum):
    REPETITION = "التكرار العددي"
    BALANCE = "التوازن العددي"
    PROPORTIONALITY = "التناسب العددي"
    CONCORDANCES = "التوافقات العددية"
    SYMMETRY = "التماثل العددي"
    PROXIMITY = "التقارب العددي"
    CRYPTICITY = "الترميز/التشفير"
    
    def __str__(self):
        return self.value

class AnalysisUnit(Enum):
    HARF = "الحرف"
    WORD = "الكلمة"
    AYAH = "الآية"
    SURAH = "السورة"
    ROOT = "الجذر"
    
    def __str__(self):
        return self.value

class NumericalSource(Enum):
    EXPLICIT_TEXT = "صريح - مكتوب نصًا"
    EXPLICIT_NUMBER = "صريح - مرقوم رقمًا"
    IMPLIED_CALCULATED = "مستنبط - محسوب (محصى)"
    IMPLIED_CODED = "مستنبط - مُرمّز"
    
    def __str__(self):
        return self.value

class HypothesisModel:
    def __init__(self, p_type, a_unit, target, scope, n_source, c_value):
        self.phenomenon_type = p_type
        self.analysis_unit = a_unit
        self.target_text = target
        self.text_scope = scope
        self.numerical_source = n_source
        self.comparison_value = c_value

    def generate_hypothesis_question(self):
        return (
            f"❓ هل {self.phenomenon_type} لـ '{self.target_text}' "
            f"كوحدة '{self.analysis_unit}' "
            f"في نطاق '{self.text_scope}' "
            f"يساوي القيمة العددية '{self.comparison_value}' (مصدر: {self.numerical_source})؟"
        )
    
    def export_study_profile(self):
        return {
            "phenomenon_type": str(self.phenomenon_type),
            "analysis_unit": str(self.analysis_unit),
            "target_text": self.target_text,
            "text_scope": self.text_scope,
            "numerical_source": str(self.numerical_source),
            "comparison_value": self.comparison_value
        }

# ====== 2. الوظيفة التفاعلية لجمع المدخلات ======

def get_choice(prompt, enum_class):
    options = list(enum_class)
    print(prompt)
    for i, member in enumerate(options):
        print(f"   [{i + 1}] {member.value}")
    
    while True:
        try:
            choice = int(input("   اختر الرقم الموافق: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("   ⚠️ الرقم المدخل خارج نطاق الخيارات. حاول مرة أخرى.")
        except ValueError:
            print("   ⚠️ إدخال غير صالح. يرجى إدخال رقم.")

def interactive_hypothesis_builder():
    print("=" * 60)
    print("           🛠️ مُنشئ الفرضيات العددية في القرآن (المرحلة 1) 🛠️")
    print("=" * 60)

    # 1. تحديد نوع الظاهرة
    p_type = get_choice("1️⃣ تحديد نوع الظاهرة العددية:", PhenomenonType)
    print(f"   👈 تم اختيار: {p_type.value}\n")

    # 2. تحديد الوحدة القرآنية
    a_unit = get_choice("2️⃣ تحديد الوحدة القرآنية للتحليل:", AnalysisUnit)
    print(f"   👈 تم اختيار: {a_unit.value}\n")

    # 3. النص المستهدف
    target = input("3️⃣ أدخل النص القرآني المستهدف للعد (مثال: 'يوم' أو 'و'): ")
    
    # 4. مجال النص
    scope = input("4️⃣ حدد مجال النص القرآني (مثال: 'القرآن كاملاً' أو 'سورة البقرة'): ")

    # 5. القيمة العددية ومصدرها
    print("\n5️⃣ تحديد القيمة العددية للمقارنة ومصدرها:")
    n_source = get_choice("   اختر مصدر القيمة العددية:", NumericalSource)
    comp_value = input(f"   أدخل القيمة العددية التي تريد اختبارها (مثال: 365): ")
    print(f"   👈 تم اختيار المصدر: {n_source.value} والقيمة: {comp_value}\n")

    # ====== 3. توليد وعرض النموذج ======
    
    study_model = HypothesisModel(p_type, a_unit, target, scope, n_source, comp_value)
    
    print("-" * 60)
    print("✅ تم إنشاء الفرضية بنجاح! هذا هو ملف تعريف الدراسة للمرحلة الثانية:")
    print("-" * 60)
    
    # عرض ملف التعريف
    profile = study_model.export_study_profile()
    print("📁 ملف تعريف الدراسة (Study Profile):")
    print(json.dumps(profile, indent=2, ensure_ascii=False)) 
    
    # عرض السؤال البحثي
    print("\n📝 السؤال البحثي النهائي:")
    print(study_model.generate_hypothesis_question())
    print("-" * 60)
    print("انتهت المرحلة الأولى. يمكنك الآن المتابعة لتحديد السياسات المرجعية.")

# تنفيذ البرنامج
if __name__ == "__main__":
    interactive_hypothesis_builder()
