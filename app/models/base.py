# 모든 모델이 상속받을 Base 클래스입니다. Alembic이 인식하기 위한 시작점입니다.
from sqlalchemy.orm import DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    __abstract__ = True
    
    # 모든 테이블에 공통으로 들어갈 컬럼 (예: 생성일, 수정일)
    created_at = Column(DateTime, default=func.now())
    created_by = Column(String(50), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    updated_by = Column(String(50), nullable=False)
    
    # 테이블명 자동 생성
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()