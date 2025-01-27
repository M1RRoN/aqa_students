from typing import ClassVar

from pydantic import BaseModel, Field, model_validator, ConfigDict

MIN_MARK = 2
MAX_MARK = 5


class GroupStatistics(BaseModel):
    avg_mark: float = Field(alias="avgMark", ge=MIN_MARK, le=MAX_MARK)
    min_mark: float = Field(alias="minMark", ge=MIN_MARK, le=MAX_MARK)
    max_mark: float = Field(alias="maxMark", ge=MIN_MARK, le=MAX_MARK)

    model_config = ConfigDict(populate_by_name=True)

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
