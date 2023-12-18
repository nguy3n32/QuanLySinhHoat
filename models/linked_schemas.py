from typing import Optional, List

from .students import StudentRead
from .parents import ParentRead


class StudentWithParent(StudentRead):
    parent: Optional["ParentRead"]


class ParentWithChild(ParentRead):
    children: List["StudentRead"] = []
