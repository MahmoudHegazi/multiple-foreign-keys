#!/usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()



class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    domain = Column(String(100), nullable=False)
    # main elements
    d_h1 = Column(String(1000))
    d_p = Column(String(3000))
    d_img = Column(String(500))
    # style section fixed values for h1 or p
    d_textcolor = Column(String(50))
    d_pagecolor = Column(String(50))
    d_background = Column(String(300))
    d_pwidth = Column(String(50))
    d_margin = Column(String(50))
    d_padding = Column(String(50))
    d_textalign = Column(String(50))
    # style section fixed image
    d_imgwidth = Column(String(500))
    d_imgheight = Column(String(50))
    d_imgradius = Column(String(50))
    d_borderwidth = Column(String(50))
    d_bordertype = Column(String(50))
    d_bordercolor = Column(String(100))
    # style section variable for h1
    h1_image = Column(String(500))
    h1_background = Column(String(50))
    h1_bradius = Column(String(50))
    h1_fsize = Column(String(50))
    h1_customsize = Column(String(100))
    h1_width = Column(String(100))
    # users comments and post
    user_post = Column(String(2000))
    comment = Column(String(2000))
    # some extra storage
    extra = Column(String(500))
    extra_string = Column(String(500))
    another_string = Column(String(500))
    last_extra = Column(String(500))
    extra_int = Column(Integer)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'title': self.title,
            'id': self.id,
            'domain': self.domain,
            'd_h1': self.d_h1,
            'd_p': self.d_p,
            'd_img': self.d_img,
            'd_textcolor': self.d_textcolor,
            'd_pagecolor': self.d_pagecolor,
            'd_background': self.d_background,
            'd_pwidth': self.d_pwidth,
            'd_margin': self.d_margin,
            'd_padding': self.d_padding,
            'd_textalign': self.d_textalign,
            'd_imgwidth': self.d_imgwidth,
            'd_imgheight': self.d_imgheight,
            'd_imgradius': self.d_imgradius,
            'd_borderwidth': self.d_borderwidth,
            'd_bordertype': self.d_bordertype,
            'd_bordercolor': self.d_bordercolor,
            'h1_image': self.h1_image,
            'h1_background': self.h1_background,
            'h1_bradius': self.h1_bradius,
            'h1_fsize': self.h1_fsize,
            'h1_customsize': self.h1_customsize,
            'h1_width': self.h1_width,
            'user_post': self.user_post,
            'comment': self.comment,
            'extra': self.extra,
            'extra_int': self.extra_int            
        }
   

class Mydocuments(Base):
    __tablename__ = 'mydocuments'

    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey('document.id'), nullable=False)
    document_domain = Column(String(100), ForeignKey('document.domain'), nullable=False)
    document = relationship("Document", foreign_keys=[document_id])
    mydocuments = relationship("Document", foreign_keys=[document_domain])
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'documentId': self.documentId,
            'document_doman': self.document_doman
        }


class Vote(Base):
    __tablename__ = 'vote'

    id = Column(Integer, primary_key=True)
    likes = Column(Integer)
    dislike = Column(Integer)    


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'likes': self.likes,
            'dislike': self.dislike,
            'id': self.id
        }
        
        
engine = create_engine('sqlite:///editor.db')
Base.metadata.create_all(engine)
