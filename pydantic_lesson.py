from pydantic import BaseModel, Field, field_validator, model_validator


class GroupStatistics(BaseModel):
    avg_mark: float = Field(alias="avgMark")
    min_mark: float = Field(alias="minMark")
    max_mark: float = Field(alias="maxMark")

    class Config:
        populate_by_name = True

    @field_validator("avg_mark", "min_mark", "max_mark")
    def check_marks_range(cls, value):
        if not (2.0 <= value <= 5.0):
            raise ValueError("Оценка должна быть в диапазоне от 2.0 до 5.0")
        return value

    @model_validator(mode="after")
    def check_avg_mark(cls, model: "GroupStatistics"):
        if model.min_mark > model.max_mark:
            raise ValueError("min_mark не может быть больше max_mark")
        if not (model.min_mark <= model.avg_mark <= model.max_mark):
            raise ValueError("avg_mark должно быть между min_mark и max_mark")
        return model


marks = [3.0, 4.0, 5.0, 2.5, 4.5, 3.5]

avg_mark = sum(marks) / len(marks)
max_mark = max(marks)
min_mark = min(marks)

statistics = GroupStatistics(avg_mark=avg_mark, max_mark=max_mark, min_mark=min_mark)

print(statistics)
