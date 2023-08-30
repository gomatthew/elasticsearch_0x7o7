from app.main import db
from app.main.lib.datetimeLib import dt


class StandardAddress(db.Model):

    __tablename__ = 'duyun_standard_address_info'
    address_logic_id = db.Column(db.String(64))
    address_detail = db.Column(db.String(64))
    address_name = db.Column(db.String(64))
    address_element_type = db.Column(db.String(8))
    ad_logic_id = db.Column(db.String(64))
    province_code = db.Column(db.String(64))
    city_code = db.Column(db.String(64))
    county_district_code = db.Column(db.String(64))
    community_village_code = db.Column(db.String(64))
    town_code = db.Column(db.String(64))
    grid_code = db.Column(db.String(64))
    block_logic_id = db.Column(db.String(64))
    platoon_building_logic_id = db.Column(db.String(64))
    unit_logic_id = db.Column(db.String(64))
    house_floor = db.Column(db.String(32))
    house_no = db.Column(db.String(32))
    longitude = db.Column(db.String(255))
    latitude = db.Column(db.String(255))
    order_flag = db.Column(db.Integer)
    has_del = db.Column(db.Integer)
    tag_name = db.Column(db.String(100))
    tag_code = db.Column(db.String(45))
    id = db.Column(db.Integer)

    def __repr__(self):
        return "<App (%s)>" % self.id
