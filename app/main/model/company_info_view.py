# -*-coding:utf-8-*-
from app.main import db


class CompanyInfo(db.Model):
    __tablename__ = 'duyun_company_info'
    id = db.Column(db.Integer)
    company_logic_id = db.Column(db.String(64))
    company_name = db.Column(db.String(64))
    company_address = db.Column(db.String(64))
    company_telephone = db.Column(db.String(20))
    company_status = db.Column(db.String(64))
    address_logic_id = db.Column(db.String(64),comment='id')
    ad_logic_id = db.Column(db.String(64))
    security_per_phone = db.Column(db.String(16))
    security_per_name = db.Column(db.String(16))
    company_type_code = db.Column(db.String(64))
    company_industrial_type = db.Column(db.String(255))
    legal_per_name = db.Column(db.String(64))
    legal_per_phone = db.Column(db.String(16))
    legal_per_certificates_type = db.Column(db.String(64))
    legal_per_certificates = db.Column(db.String(64))
    img_url = db.Column(db.String(256))
    ent_code = db.Column(db.String(64))
    employers_number = db.Column(db.String(64))
    has_condition_party_org = db.Column(db.String(64))
    has_party_org = db.Column(db.String(8))
    party_member_num = db.Column(db.Integer)
    social_organization_code = db.Column(db.String(64))
    has_trunde_union = db.Column(db.Integer)
    trunde_member_num = db.Column(db.Integer)
    has_comm_younth_league = db.Column(db.String(8))
    comm_younth_league_num = db.Column(db.Integer)
    women_federation_num = db.Column(db.Integer)
    has_women_federation = db.Column(db.String(8))
    company_info_has_del = db.Column(db.String(8))
    server_default = db.text("")
    has_hazardous_chemical = db.Column(db.String(8))
    type_hidden_danger = db.Column(db.String(8))
    degree_concern = db.Column(db.String(64))
    data_source = db.Column(db.String(64))
    bp_name = db.Column(db.String(64))
    bp_code = db.Column(db.String(64))
    building_block_info_has_del = db.Column(db.Integer)
    community_name = db.Column(db.String(64))
    platoon_no = db.Column(db.String(64))
    building_info_has_del = db.Column(db.Integer)
    address_detail = db.Column(db.String(64))
    address_name = db.Column(db.String(64))
    address_element_type = db.Column(db.String(8))
    province_code = db.Column(db.String(64))
    city_code = db.Column(db.String(64))
    county_district_code = db.Column(db.String(64))
    town_code = db.Column(db.String(64))
    community_village_code = db.Column(db.String(64))
    grid_code = db.Column(db.String(64))
    block_logic_id = db.Column(db.String(64))
    platoon_building_logic_id = db.Column(db.String(64))
    unit_logic_id = db.Column(db.String(64))
    house_floor = db.Column(db.String(32))
    house_no = db.Column(db.String(32))
    longitude = db.Column(db.String(255))
    latitude = db.Column(db.String(255))
    standard_address_has_del = db.Column(db.Integer)
    order_flag = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)