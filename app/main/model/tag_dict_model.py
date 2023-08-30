# -*-coding:utf-8-*-
from app.main import db
from app.main.lib.datetimeLib import dt


class TagDict(db.Model):
    __tablename__ = 'tag_dict'
    id = db.Column(db.Integer, primary_key=True,  comment='id')
    dict_logic_id = db.Column(db.String(60), nullable=False, comment='逻辑主键')
    tag_name = db.Column(db.String(100), nullable=False, comment='标签名')
    tag_code = db.Column(db.String(45), nullable=False, comment='数据值')
    tag_type_code = db.Column(db.String(45), nullable=False, comment='类型代码')
    tag_type_name = db.Column(db.String(45), nullable=False, comment='类型名称')
    order_num = db.Column(db.Integer, nullable=False, comment='排序（升序）')
    parent_code = db.Column(db.String(45), nullable=False, comment='父级编号')
    remarks = db.Column(db.String(255), nullable=False, comment='备注信息')
    has_del = db.Column(db.String(45), nullable=False, comment='数据值')
    create_user = db.Column(db.String(100), nullable=False, comment='创建者账号')
    update_user = db.Column(db.String(100), nullable=False, comment='更新者账号')
    # create time
    create_time = db.Column(db.DateTime, default=dt.method_datetime, comment='创建时间')
    # update time
    update_time = db.Column(db.DateTime, default=dt.method_datetime, onupdate=dt.method_datetime, comment='更新时间')

    def __repr__(self):
        return "<App (%s)>" % self.id
