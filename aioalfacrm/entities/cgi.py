import datetime
from typing import Optional

from .. import fields
from ..core import AlfaEntity


class CGI(AlfaEntity):
    id: Optional[int] = fields.Integer()
    customer_id: Optional[int] = fields.Integer()
    group_id: Optional[int] = fields.Integer()
    b_date: Optional[datetime.date] = fields.DateField()
    e_date: Optional[datetime.date] = fields.DateField()

    def __init__(
            self,
            id_: Optional[int] = None,
            customer_id: Optional[int] = None,
            group_id: Optional[int] = None,
            b_date: Optional[datetime.date] = None,
            e_date: Optional[datetime.date] = None,
            **kwargs,
    ):
        super().__init__(
            id=id_,
            customer_id=customer_id,
            group_id=group_id,
            b_date=b_date,
            e_date=e_date,
            **kwargs,
        )
