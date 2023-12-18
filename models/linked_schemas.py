from typing import Optional, List

from .students import StudentRead
from .parents import ParentRead
from .mentors import MentorsRead
from .courses import CoursesRead


class StudentWithParent(StudentRead):
    parent: Optional["ParentRead"]


class ParentWithChild(ParentRead):
    children: List["StudentRead"] = []


class MentorsWithCourses(MentorsRead):
    courses: List["CoursesRead"] = []


class CoursesWithMentors(CoursesRead):
    mentors: List["MentorsRead"] = []
