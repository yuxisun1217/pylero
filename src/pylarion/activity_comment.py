# -*- coding: utf8 -*-
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals
import pylarion.base_polarion as bp
import pylarion.text as t


class ActivityComment(bp.BasePolarion):
    """Object to handle the Polarion WSDL tns3:ActivityComment class

    Attributes (for specific details, see Polarion):
        text (Text)
        time_stamp (dateTime)
        user_id (string)
"""
    _cls_suds_map = {"text": {"field_name": "text", "cls": t.Text},
                     "time_stamp": "timeStamp",
                     "user_id": "userId",
                     "uri": "_uri",
                     "_unresolved": "_unresolved"}
    _obj_client = "tracker_client"
    _obj_struct = "tns3:ActivityComment"
