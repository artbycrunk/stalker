# -*- coding: utf-8 -*-
# Copyright (c) 2009-2012, Erkan Ozgur Yilmaz
# 
# This module is part of Stalker and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause

from sqlalchemy import Column, Integer, ForeignKey, String
from stalker.models.entity import Entity
from stalker.models.mixins import TargetEntityTypeMixin

class Type(Entity, TargetEntityTypeMixin):
    """Everything can have a type.
    
    .. versionadded:: 0.1.1
      Types
    
    Type is a generalized version of the previous design that defines types for
    specific classes.
    
    The purpose of the :class:`~stalker.models.type.Type` class is just to
    define a new type for a specific :class:`~stalker.models.entity.Entity`.
    For example, you can have a ``Character``
    :class:`~stalker.models.asset.Asset` or you can have a ``Commercial``
    :class:`~stalker.models.project.Project` or you can define a
    :class:`~stalker.models.link.Link` as an ``Image`` etc.,
    to create a new :class:`~stalker.models.type.Type` for various classes::
    
      Type(name="Character", target_entity_type="Asset")
      Type(name="Commercial", target_entity_type="Project")
      Type(name="Image", target_entity_type="Link")
    
    or::
      
      Type(name="Character", target_entity_type=Asset.entity_type)
      Type(name="Commercial", target_entity_type=Project.entity_type)
      Type(name="Image", target_entity_type=Link.entity_type)
    
    or even better:
      
      Type(name="Character", target_entity_type=Asset)
      Type(name="Commercial", target_entity_type=Project)
      Type(name="Image", target_entity_type=Link)
    
    By using :class:`~stalker.models.type.Type`\ s, one can able to sort and
    group same type of entities.
    
    :class:`~stalker.models.type.Type`\ s are generally used in
    :class:`~stalker.models.type.Structure`\ s.
    
    :param string target_entity_type: The string defining the target type of
      this :class:`~stalker.models.type.Type`.
    """

    __tablename__ = "Types"
    __mapper_args__ = {"polymorphic_identity": "Type"}
    type_id_local = Column("id", Integer, ForeignKey("Entities.id"),
                           primary_key=True)
    _target_entity_type = Column(
        "target_entity_type",
        String
    )

    def __init__(self, **kwargs):
        super(Type, self).__init__(**kwargs)
        TargetEntityTypeMixin.__init__(self, **kwargs)
#        self._target_entity_type =\
#        self._validate_target_entity_type(target_entity_type)
    
    def __eq__(self, other):
        """the equality operator
        """

        return super(Type, self).__eq__(other) and isinstance(other, Type)\
        and self.target_entity_type == other.target_entity_type

    def __ne__(self, other):
        """the inequality operator
        """

        return not self.__eq__(other)