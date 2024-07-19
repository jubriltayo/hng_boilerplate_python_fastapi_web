#!/usr/bin/env python3
""" Base
"""
from sqlalchemy import (
        Column,
        Integer,
        ForeignKey,
        Table
        )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID


Base = declarative_base()

user_organization_association = Table('user_organization', Base.metadata,
        Column('user_id', UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True),
        Column('organization_id', UUID(as_uuid=True), ForeignKey('organizations.id'), primary_key=True)
        )

class BaseModel():
    """ This model creates helper methods for all models
    """
    def to_dict(self):
        """ returns a dictionary representation of the instance
        """
        obj_dict = self.__dict__.copy()
        del obj_dict["_sa_instance_state"]
        obj_dict['id'] = str(self.id)
        if self.created_at:
            obj_dict["created_at"] = self.created_at.isoformat()
        if self.updated_at:
            obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    @classmethod
    def get_all(cls):
        """ returns all instance of the class in the db
        """
        from api.db.database import db
        return db.query(cls).all()

    @classmethod
    def get_by_id(cls, id):
        """ returns a single object from the db
        """
        from api.db.database import db
        obj = db.query(cls).filter_by(id=id).first()
        return obj
