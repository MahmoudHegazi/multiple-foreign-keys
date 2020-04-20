# multiple-foreign-keys
SQLAlchemy multiple foreign keys in one mapped class to the same primary key


```python
class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    domain = Column(String(100), nullable=False)
    
    
class Mydocuments(Base):
    __tablename__ = 'mydocuments'

    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey('document.id'), nullable=False)
    document_domain = Column(String(100), ForeignKey('document.domain'), nullable=False)
    document = relationship("Document", foreign_keys=[document_id])
    mydocuments = relationship("Document", foreign_keys=[document_domain])
    mydocuments = relationship("Document", foreign_keys=[document_id])
```    
