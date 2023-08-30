import faker
import random
from uuid import uuid1
from datetime import datetime
from app.main.model.tag_dict_model import TagDict

fake = faker.Faker('zh_CN')
fake_foreigner = faker.Faker('en_US')

nation = TagDict.query.filter(TagDict.tag_type_code == 'nation').all()
gender = TagDict.query.filter(TagDict.tag_type_code == 'gender').all()
marriage = TagDict.query.filter(TagDict.tag_type_code == 'marital_status').all()
education_type = TagDict.query.filter(TagDict.tag_type_code == 'education_type').all()
political = TagDict.query.filter(TagDict.tag_type_code == 'politic_countenance').all()
religious = TagDict.query.filter(TagDict.tag_type_code == 'religious_belief').all()
career = TagDict.query.filter(TagDict.tag_type_code == 'company_type').all()
relation = TagDict.query.filter(TagDict.tag_type_code == 'guardian_relationship').all()
file = TagDict.query.filter(TagDict.tag_type_code == 'file_type').all()
consistent_identification = TagDict.query.filter(TagDict.tag_type_code == 'consistent_identification').all()
id_card_type = TagDict.query.filter(TagDict.tag_type_code == 'id_card_type').all()
hukou_type = TagDict.query.filter(TagDict.tag_type_code == 'hukou_type').all()
personnel_type = TagDict.query.filter(TagDict.tag_type_code == 'personnel_type').all()
inflow_reason = TagDict.query.filter(TagDict.tag_type_code == 'inflow_reason').all()
residence_type = TagDict.query.filter(TagDict.tag_type_code == 'residence_type').all()
health_status = TagDict.query.filter(TagDict.tag_type_code == 'health_status').all()
relationship_household = TagDict.query.filter(TagDict.tag_type_code == 'relationship_household').all()
foreigners_reason_to_china = TagDict.query.filter(TagDict.tag_type_code == 'foreigners_reason_to_china').all()
sin_type = TagDict.query.filter(TagDict.tag_type_code == 'sin_type').all()
risk_assessment_type = TagDict.query.filter(TagDict.tag_type_code == 'risk_assessment_type').all()
connection_situation = TagDict.query.filter(TagDict.tag_type_code == 'connection_situation').all()
placement_situation = TagDict.query.filter(TagDict.tag_type_code == 'placement_situation').all()
help_situation = TagDict.query.filter(TagDict.tag_type_code == 'help_situation').all()
correction_type = TagDict.query.filter(TagDict.tag_type_code == 'correction_type').all()
receiving_type = TagDict.query.filter(TagDict.tag_type_code == 'receiving_type').all()
three_involved = TagDict.query.filter(TagDict.tag_type_code == 'three_involved').all()
correction_group_type = TagDict.query.filter(TagDict.tag_type_code == 'correction_group_type').all()


# correction_type = TagDict.query.filter(TagDict.tag_type_code == 'correction_type').all()


def get_tag_dict(tag_name):
    match tag_name:
        case 'nation':
            nat = random.choice(nation)
            return nat.tag_code, nat.tag_name
        case 'gender':
            gen = random.choice(gender)
            return gen.tag_code, gen.tag_name
        case 'marital_status':
            mar = random.choice(marriage)
            return mar.tag_code, mar.tag_name
        case 'education_type':
            edu = random.choice(education_type)
            return edu.tag_code, edu.tag_name
        case 'politic_countenance':
            po = random.choice(political)
            return po.tag_code, po.tag_name
        case 'religious_belief':
            rel = random.choice(religious)
            return rel.tag_code, rel.tag_name
        case 'career':
            car = random.choice(career)
            return car.tag_code, car.tag_name
        case 'relation':
            rel = random.choice(relation)
            return rel.tag_code, rel.tag_name
        case 'file_type':
            fi = random.choice(file)
            return fi.tag_code, fi.tag_name
        case 'consistent_identification':
            co = random.choice(consistent_identification)
            return co.tag_code, co.tag_name
        case 'id_card_type':
            id = random.choice(id_card_type)
            return id.tag_code, id.tag_name
        case 'hukou_type':
            hu = random.choice(hukou_type)
            return hu.tag_code, hu.tag_name
        case 'personnel_type':
            per = random.choice(personnel_type)
            return per.tag_code, per.tag_name
        case 'inflow_reason':
            inn = random.choice(inflow_reason)
            return inn.tag_code, inn.tag_name
        case 'residence_type':
            res = random.choice(residence_type)
            return res.tag_code, res.tag_name
        case 'health_status':
            res = random.choice(health_status)
            return res.tag_code, res.tag_name
        case 'relationship_household':
            res = random.choice(relationship_household)
            return res.tag_code, res.tag_name
        case 'foreigners_reason_to_china':
            res = random.choice(foreigners_reason_to_china)
            return res.tag_code, res.tag_name
        case 'sin_type':
            res = random.choice(sin_type)
            return res.tag_code, res.tag_name
        case 'risk_assessment_type':
            res = random.choice(risk_assessment_type)
            return res.tag_code, res.tag_name
        case 'connection_situation':
            res = random.choice(connection_situation)
            return res.tag_code, res.tag_name
        case 'placement_situation':
            res = random.choice(placement_situation)
            return res.tag_code, res.tag_name
        case 'help_situation':
            res = random.choice(help_situation)
            return res.tag_code, res.tag_name
        case 'correction_type':
            res = random.choice(correction_type)
            return res.tag_code, res.tag_name
        case 'receiving_type':
            res = random.choice(receiving_type)
            return res.tag_code, res.tag_name
        case 'three_involved':
            res = random.choice(three_involved)
            return res.tag_code, res.tag_name
        case 'correction_group_type':
            res = random.choice(correction_group_type)
            return res.tag_code, res.tag_name
        case 'correction_type':
            res = random.choice(correction_type)
            return res.tag_code, res.tag_name
    # if tag_name == 'nation':
    #     nat = random.choice(nation)
    #     return nat.tag_code, nat.tag_name
    # elif tag_name == 'gender':
    #     gen = random.choice(gender)
    #     return gen.tag_code, gen.tag_name
    # elif tag_name == 'marital_status':
    #     mar = random.choice(marriage)
    #     return mar.tag_code, mar.tag_name
    # elif tag_name == 'education_type':
    #     edu = random.choice(education_type)
    #     return edu.tag_code, edu.tag_name
    # elif tag_name == 'politic_countenance':
    #     po = random.choice(political)
    #     return po.tag_code, po.tag_name
    # elif tag_name == 'religious_belief':
    #     rel = random.choice(religious)
    #     return rel.tag_code, rel.tag_name
    # elif tag_name == 'career':
    #     car = random.choice(career)
    #     return car.tag_code, car.tag_name
    # elif tag_name == 'relation':
    #     rel = random.choice(relation)
    #     return rel.tag_code, rel.tag_name
    # elif tag_name == 'file_type':
    #     fi = random.choice(file)
    #     return fi.tag_code, fi.tag_name
    # elif tag_name == 'consistent_identification':
    #     co = random.choice(consistent_identification)
    #     return co.tag_code, co.tag_name
    # elif tag_name == 'id_card_type':
    #     id = random.choice(id_card_type)
    #     return id.tag_code, id.tag_name
    # elif tag_name == 'hukou_type':
    #     hu = random.choice(hukou_type)
    #     return hu.tag_code, hu.tag_name
    # elif tag_name == 'personnel_type':
    #     per = random.choice(personnel_type)
    #     return per.tag_code, per.tag_name
    # elif tag_name == 'inflow_reason':
    #     inn = random.choice(inflow_reason)
    #     return inn.tag_code, inn.tag_name
    # elif tag_name == 'residence_type':
    #     res = random.choice(residence_type)
    #     return res.tag_code, res.tag_name
    # elif tag_name == 'health_status':
    #     res = random.choice(health_status)
    #     return res.tag_code, res.tag_name
    # elif tag_name == 'relationship_household':
    #     res = random.choice(relationship_household)
    #     return res.tag_code, res.tag_name
    # elif tag_name == 'foreigners_reason_to_china':
    #     res = random.choice(foreigners_reason_to_china)
    #     return res.tag_code, res.tag_name
    # elif tag_name == 'sin_type':
    #     res = random.choice(sin_type)
    #     return res.tag_code, res.tag_name
    # elif tag_name == 'risk_assessment_type':
    #     res = random.choice(risk_assessment_type)
    #     return res.tag_code, res.tag_name
    # elif tag_name == 'connection_situation':
    #     res = random.choice(connection_situation)
    #     return res.tag_code, res.tag_name
    # elif tag_name == 'placement_situation':
    #     res = random.choice(placement_situation)
    #     return res.tag_code, res.tag_name
    # elif tag_name == 'help_situation':
    #     res = random.choice(help_situation)
    #     return res.tag_code, res.tag_name
    # elif tag_name == 'correction_type':
    #     res = random.choice(correction_type)
    #     return res.tag_code, res.tag_name
    # elif tag_name == 'receiving_type':
    #     res = random.choice(receiving_type)
    #     return res.tag_code, res.tag_name
    # elif tag_name == 'three_involved':
    #     res = random.choice(three_involved)
    #     return res.tag_code, res.tag_name
    # elif tag_name == 'correction_group_type':
    #     res = random.choice(correction_group_type)
    #     return res.tag_code, res.tag_name
    # elif tag_name == 'correction_type':
    #     res = random.choice(correction_type)
    #     return res.tag_code, res.tag_name


def gen_person():
    gender = get_tag_dict('gender')
    nation = get_tag_dict('nation')
    political = get_tag_dict('politic_countenance')
    marriage = get_tag_dict('marital_status')
    edu = get_tag_dict('education_type')
    religious = get_tag_dict('religious_belief')
    career = get_tag_dict('career')
    relation = get_tag_dict('relation')
    file = get_tag_dict('file_type')
    consistent_identification = get_tag_dict('consistent_identification')
    id_card_type = get_tag_dict('id_card_type')
    hukou_type = get_tag_dict('hukou_type')
    personnel_type = get_tag_dict('personnel_type')
    inflow_reason = get_tag_dict('inflow_reason')
    residence_type = get_tag_dict('residence_type')
    health_status = get_tag_dict('health_status')
    relationship_household = get_tag_dict('relationship_household')
    foreigners_reason_to_china = get_tag_dict('foreigners_reason_to_china')
    sin_type = get_tag_dict('sin_type')
    risk_assessment_type = get_tag_dict('risk_assessment_type')
    connection_situation = get_tag_dict('connection_situation')
    placement_situation = get_tag_dict('placement_situation')
    help_situation = get_tag_dict('help_situation')
    correction_type = get_tag_dict('correction_type')
    receiving_type = get_tag_dict('receiving_type')
    three_involved = get_tag_dict('three_involved')
    correction_group_type = get_tag_dict('correction_group_type')
    person = {
        'id': str(uuid1()),
        'person_logic_id': fake.ssn(),
        'person_id': fake.ssn(),
        'person_name': fake.name(),
        'person_name_before': fake.name(),
        'gender': gender[0],
        'gender_name': gender[1],
        'birthday': fake.date_of_birth(),
        'phone': fake.phone_number(),
        'nation': nation[0],
        'nation_name': nation[1],
        'marriage_status': marriage[0],
        'marriage_status_name': marriage[1],
        'degree_of_education': edu[0],
        'degree_of_education_name': edu[1],
        'height': random.randint(160, 185),
        'native_place': fake.city(),
        'political_outlook': political[0],
        'political_outlook_name': political[1],
        'religious_belief': religious[0],
        'religious_belief_name': religious[1],
        'career_type': career[0],
        'career_type_name': career[1],
        'career': career[0],
        'career_name': career[1],
        'ad_logic_id': fake.address(),
        'register_address': fake.address(),
        'register_address_detail': fake.address(),
        'register_address_logic_id': fake.address(),
        'person_house_relation_logic_id': str(uuid1()),
        'relation_type': relation[0],
        'relation_type_name': relation[1],
        'house_logic_id': fake.ssn(),
        'live_address': fake.address(),
        'live_address_detail': fake.address(),
        'live_address_logic_id': str(uuid1()),
        'job_address_detail': fake.address(),
        'job_address_logic_id': str(uuid1()),
        'create_user': '0x7o7',
        'update_user': '0x7o7',
        'create_time': datetime.now().strftime('%Y-%m-%d %X'),
        'update_time': datetime.now().strftime('%Y-%m-%d %X'),
        'person_company_relation_logic_id': str(uuid1()),
        'company_logic_id': str(uuid1()),
        'block_logic_id': str(uuid1()),
        'platoon_building_logic_id': str(uuid1()),
        'unit_logic_id': str(uuid1()),
        'file_logic_id': str(uuid1()),
        'file_object_type': file[0],
        'file_object_type_name': file[1],
        'file_object_id': str(uuid1()),
        'file_type': file[0],
        'file_type_name': file[1],
        'file_name': '0x7o7',
        'file_path': fake.file_path(depth=3, category=None, extension=None),
        'data_source': '0x7o7',
        'consistent_identification': consistent_identification[0],
        'consistent_identification_name': consistent_identification[1],
        'id_card_type': id_card_type[0],
        'id_card_type_name': id_card_type[1],
        'registered_person_flag': random.randint(0, 1),
        'hukou_code': hukou_type[0],
        'hukou_name': hukou_type[1],
        'householder_id': fake.ssn(),
        'registered_person_type_code': personnel_type[0],
        'registered_person_type_name': personnel_type[1],
        'floating_person_flag': random.randint(0, 1),
        'inflow_reason': inflow_reason[0],
        'inflow_reason_name': inflow_reason[1],
        'floating_person_card_code': fake.ssn(),
        'registration_date': fake.date_time().strftime('%Y-%m-%d %X'),
        'floating_due_date': fake.date_time().strftime('%Y-%m-%d %X'),
        'residence_type': residence_type[0],
        'residence_type_name': residence_type[1],
        'focus_person_flg': random.randint(0, 1),
        'health_status': health_status[0],
        'health_status_name': health_status[1],
        'rear_person_flag': random.randint(0, 1),
        'annual_personal_income': random.randint(5000, 100000),
        # 'rear_person_type': {"type": "keyword"},
        # 'rear_person_type_name': {"type": "keyword"},
        'primary_member_id': fake.ssn(),
        'primary_member_name': fake.name(),
        'primary_member_health_status': health_status[0],
        'primary_member_health_status_name': health_status[1],
        'relationship_with_rear': relationship_household[0],
        'relationship_with_rear_name': relationship_household[1],
        'primary_member_phone': fake.phone_number(),
        'primary_member_work_address': fake.address(),
        'annual_family_income': random.randint(5000, 100000),
        # 'difficulties_and_demands': {"type": "keyword"},
        'has_del': random.randint(0, 1),
        'foreigner_flag': random.randint(0, 1),
        'foreign_surname': fake_foreigner.first_name(),
        'foreign_name': fake_foreigner.name(),
        'chinese_name': fake.name(),
        'nationality': nation[0],
        'country_name': nation[1],
        'foreigners_card_code': fake_foreigner.ssn(),
        'foreigners_due_date': fake.date_time().strftime('%Y-%m-%d %X'),
        'reason_to_china': foreigners_reason_to_china[0],
        'reason_to_china_name': foreigners_reason_to_china[1],
        'company_name': fake.company(),
        'arrival_date': fake.date_time().strftime('%Y-%m-%d %X'),
        'estimated_departure_date': fake.date_time().strftime('%Y-%m-%d %X'),
        'release_person_flag': random.randint(0, 1),
        'recidivism_flag': random.randint(0, 1),
        'original_sin': sin_type[0],
        'original_sin_name': sin_type[1],
        'original_sentence': fake.province(),
        'place_of_sentence': fake.province(),
        'release_date': fake.date_time().strftime('%Y-%m-%d %X'),
        'risk_assessment_type': risk_assessment_type[0],
        'risk_assessment_name': risk_assessment_type[1],
        'connection_date': fake.date_time().strftime('%Y-%m-%d %X'),
        'connection_situation': connection_situation[0],
        'connection_situation_name': connection_situation[1],
        'placement_date': fake.date_time().strftime('%Y-%m-%d %X'),
        'placement_situation': placement_situation[0],
        'placement_situation_name': placement_situation[1],
        'reason_for_non_placement': '你猜',
        'release_help_situation': help_situation[0],
        'release_help_situation_name': help_situation[1],
        'crime_again_flag': random.randint(0, 1),
        'recidivism_sin': sin_type[0],
        'recidivism_sin_name': sin_type[1],
        'community_correction_person_flag': random.randint(0, 1),
        'original_detention_place': fake.province(),
        'correction_type': correction_type[0],
        'correction_type_name': correction_type[1],
        'correction_person_sin_type': sin_type[0],
        'correction_person_sin_detailed': sin_type[1],
        'correction_person_original_sentence': '',
        'original_sentence_start_date': fake.date_time().strftime('%Y-%m-%d %X'),
        'original_sentence_end_date': fake.date_time().strftime('%Y-%m-%d %X'),
        'correction_start_date': fake.date_time().strftime('%Y-%m-%d %X'),
        'correction_end_date': fake.date_time().strftime('%Y-%m-%d %X'),
        'receiving_type': receiving_type[0],
        'receiving_type_name': receiving_type[1],
        # 'four_histories': {"type": "keyword"},
        # 'four_histories_name': {"type": "keyword"},
        'three_involved': three_involved[0],
        'three_involved_name': three_involved[1],
        'has_correction_group': random.randint(0, 1),
        'correction_group_type': correction_group_type[0],
        'correction_group_type_name': correction_group_type[1],
        'correction_release_type': correction_type[0],
        'correction_release_type_name': correction_type[1],
        'escape_control_flag': random.randint(0, 1),
        # 'reason_escape_control': {"type": "keyword"},
        # 'supervision_escape_control': {"type": "keyword"},
        # 'correction_escape_control': {"type": "keyword"},
        'leakage_flag': random.randint(0, 1),
        # 'reason_leakage': {"type": "keyword"},
        # 'supervision_leakage': {"type": "keyword"},
        # 'correction_leakage': {"type": "keyword"},
        # 'rewards_punishments': {"type": "keyword"},
        # 'penalty_change': {"type": "keyword"},
        # 'severe_mental_disorders_person_flag': {"type": "keyword"},
        # 'family_economic_status': {"type": "keyword"},
        # 'subsistence_allowance_flag': {"type": "keyword"},
        # 'guardian_id': {"type": "keyword"},
        # 'guardian_name': {"type": "keyword"},
        # 'guardian_phone': {"type": "keyword"},
        # 'first_onset_date': {"type": "date", "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"},
        # 'current_diagnostic_type': {"type": "keyword"},
        # 'current_diagnostic_type_name': {"type": "keyword"},
        # 'trouble_flag': {"type": "keyword"},
        # 'trouble_cnt': {"type": "keyword"},
        # 'last_trouble_date': {"type": "date", "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"},
        # 'current_danger_level': {"type": "keyword"},
        # 'current_danger_level_name': {"type": "keyword"},
        # 'treatment_situation': {"type": "keyword"},
        # 'treatment_situation_name': {"type": "keyword"},
        # 'treatment_hospital': {"type": "keyword"},
        # 'hospitalized_reason': {"type": "keyword"},
        # 'hospitalized_reason_name': {"type": "keyword"},
        # 'rehabilitation_training_institutions': {"type": "keyword"},
        # 'participating_managers': {"type": "keyword"},
        # 'participating_managers_name': {"type": "keyword"},
        # 'found_first_date': {"type": "keyword"},
        # 'control_situation': {"type": "keyword"},
        # 'control_situation_name': {"type": "keyword"},
        # 'drug_addict_flag': {"type": "keyword"},
        # 'controller_name': {"type": "keyword"},
        # 'controller_phone': {"type": "keyword"},
        # 'drug_addict_helper_name': {"type": "keyword"},
        # 'drug_addict_helper_phone': {"type": "keyword"},
        # 'drug_addict_crime_flag': {"type": "keyword"},
        # 'drug_addict_crime_situation': {"type": "keyword"},
        # 'drug_reason': {"type": "keyword"},
        # 'drug_result': {"type": "keyword"},
        # 'AIDS_risk_person_flag': {"type": "keyword"},
        # 'infection_route': {"type": "keyword"},
        # 'infection_route_name': {"type": "keyword"},
        # 'aids_crime_flag': {"type": "keyword"},
        # 'aids_crime_situation': {"type": "keyword"},
        # 'aids_sin_type': {"type": "keyword"},
        # 'degree_concern': {"type": "keyword"},
        # 'degree_concern_name': {"type": "keyword"},
        # 'receiving_cure_situation': {"type": "keyword"},
        # 'receiving_cure_situation_name': {"type": "keyword"},
        # 'receiving_cure_institution': {"type": "keyword"},
        # 'AIDS_help_situation': {"type": "keyword"},
        # 'AIDS_helper_name': {"type": "keyword"},
        # 'AIDS_helper_phone': {"type": "keyword"},
        # 'key_teenagers_flag': {"type": "keyword"},
        # 'teenagers_type': {"type": "keyword"},
        # 'teenagers_type_name': {"type": "keyword"},
        # 'family_situation': {"type": "keyword"},
        # 'family_situation_name': {"type": "keyword"},
        # 'guardian_relationship': {"type": "keyword"},
        # 'guardian_relationship_name': {"type": "keyword"},
        # 'guardian_address': {"type": "keyword"},
        # 'teenagers_help_situation': {"type": "keyword"},
        # 'teenagers_help_method': {"type": "keyword"},
        # 'teenagers_helper_name': {"type": "keyword"},
        # 'teenagers_helper_phone': {"type": "keyword"},
        # 'address_detail': {"type": "keyword"},
        # 'address_name': {"type": "keyword"},
        # 'address_element_type': {"type": "keyword"},
        # 'address_element_name': {"type": "keyword"},
        # 'province_code': {"type": "keyword"},
        # 'city_code': {"type": "keyword"},
        # 'county_district_code': {"type": "keyword"},
        # 'town_code': {"type": "keyword"},
        # 'community_village_code': {"type": "keyword"},
        # 'grid_code': {"type": "keyword"},
        # 'road_name': {"type": "keyword"},
        # 'road_child_name': {"type": "keyword"},
        # 'community_name': {"type": "keyword"},
        # 'house_floor': {"type": "keyword"},
        # 'house_no': {"type": "keyword"},
        'longitude': fake.longitude(),
        'latitude': fake.latitude(),
        # 'order_flag': {"type": "long"}
    }
    return person


