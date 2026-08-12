
from datetime import timedelta

from feast import Entity, FeatureView, Field
from feast.infra.offline_stores.file_source import FileSource
from feast.types import Float32, Int64


# ==========================================
# 1. ENTITY
# ==========================================

graduate = Entity(
    name="reg_number",
    join_keys=["REG_Number"],
    description="Unique registration number of a CSE graduate"
)


# ==========================================
# 2. DATA SOURCE
# ==========================================

skill_gap_source = FileSource(
    path="../feature_data.parquet",
    timestamp_field="event_timestamp"
)


# ==========================================
# 3. FEATURE VIEW
# ==========================================

graduate_skill_features = FeatureView(
    name="graduate_skill_features",
    entities=[graduate],
    ttl=timedelta(days=3650),
    schema=[
        Field(name="CGPA", dtype=Float32),
        Field(name="Internship_Months", dtype=Int64),
        Field(name="Projects_Count", dtype=Int64),
        Field(name="Certifications_Count", dtype=Int64),

        Field(name="Python_Skill", dtype=Float32),
        Field(name="SQL_Skill", dtype=Float32),
        Field(name="DSA_Skill", dtype=Float32),
        Field(name="DBMS_Skill", dtype=Float32),
        Field(name="OOP_Skill", dtype=Float32),

        Field(
            name="Cloud_Computing_Skill",
            dtype=Float32
        ),

        Field(
            name="Machine_Learning_Skill",
            dtype=Float32
        ),

        Field(
            name="Communication_Skill",
            dtype=Float32
        ),

        Field(
            name="Problem_Solving_Skill",
            dtype=Float32
        ),

        Field(
            name="Overall_Skill_Gap",
            dtype=Float32
        ),

        Field(
            name="Skill_Alignment_Percentage",
            dtype=Float32
        ),

        Field(
            name="High_Priority_Gap_Count",
            dtype=Int64
        ),

        Field(
            name="Employability_Score",
            dtype=Float32
        ),
    ],
    source=skill_gap_source,
    online=True,
    description="CSE graduate curriculum-industry skill alignment features"
)
