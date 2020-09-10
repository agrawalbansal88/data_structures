import mongoengine as me
import datetime
from get_helm_data import get_changeset
from constant_values import MONGO_IP
DATABASE= "mydatabase"

class DashboardInfo(me.Document):
    name = me.StringField(required=True)
    jenkins_server = me.StringField(required=True)
    build_server = me.StringField(required=True)
    suits = me.ListField(me.StringField())
    branches = me.ListField(me.StringField())
    created_on = me.DateTimeField(required=True, default=datetime.datetime.utcnow)
    meta = dict(collection='dashboard_info')

class SuiteInfo(me.Document):
    dashboard = me.StringField(required=True)
    suite_name = me.StringField(required=True)
    build_number = me.IntField(required=True)
    failed_count = me.IntField(required=True)
    passed_count = me.IntField(required=True)
    #total_count = me.IntField(required=True)
    executed_on = me.DateTimeField(required=True)
    created_on = me.DateTimeField(required=True, default=datetime.datetime.utcnow)
    build_ref  =me.StringField()
    branch = me.StringField(required=True)
    indexes = [{'fields': ['dashboard', 'suite_name', 'branch']}]
    meta = dict(collection='suite_info')

    @classmethod
    def get_suites(cls, suite_name):
        return SuiteInfo.objects(suite_name=suite_name)

class TestInfo(me.Document):
    dashboard = me.StringField(required=True)
    suite_name = me.StringField(required=True)
    build_number = me.IntField(required=True)
    test_case = me.StringField(required=True)
    test_url = me.StringField(required=True)
    status = me.StringField(required=True)
    passed_steps = me.IntField(required=True)
    failed_steps = me.IntField(required=True)
    skipped_steps = me.IntField(required=True)
    cucumber_link = me.StringField(required=True)
    executed_on = me.DateTimeField(required=True)
    created_on = me.DateTimeField(required=True, default=datetime.datetime.utcnow)
    build_ref  =me.StringField()
    branch = me.StringField(required=True)
    indexes = [{'fields': ['dashboard', 'suite_name', 'test_case', 'branch']}]
    meta = dict(collection='test_info')

    @classmethod
    def get_tests(cls, suite_name, test_case):
        return SuiteInfo.objects(suite_name=suite_name, test_case=test_case)


class BuildInfo(me.Document):
    smf_service_build_id = me.StringField()
    smf_restep_build_id = me.StringField()
    smf_nodemgr_build_id = me.StringField()
    smf_protocol_build_id = me.StringField()
    smf_configuration_build_id = me.StringField()
    smf_ops_center_build_id = me.StringField()
    smf_egtpep_build_id = me.StringField()
    smf_upd_proxy_build_id = me.StringField()

    smf_service_commit_id = me.StringField()
    smf_restep_commit_id = me.StringField()
    smf_nodemgr_commit_id = me.StringField()
    smf_protocol_commit_id = me.StringField()
    smf_configuration_commit_id = me.StringField()
    smf_ops_center_commit_id = me.StringField()
    smf_egtpep_commit_id = me.StringField()
    smf_upd_proxy_commit_id = me.StringField()

    created_on = me.DateTimeField(required=True, default=datetime.datetime.utcnow)
    meta = dict(collection='build_info')


class CommitInfo(me.EmbeddedDocument):
    commit_id = me.StringField()
    commit_date = me.DateTimeField()
    commit_autour = me.StringField()
    commit_url = me.StringField()
    comment = me.StringField()

class BuildCommitInfo(me.Document):
    ref_id = me.StringField()
    notes = me.StringField()
    smf_service_commits = me.ListField(me.EmbeddedDocumentField(CommitInfo))
    smf_restep_commits = me.ListField(me.EmbeddedDocumentField(CommitInfo))
    smf_protocol_commits = me.ListField(me.EmbeddedDocumentField(CommitInfo))
    smf_nodemgr_commits = me.ListField(me.EmbeddedDocumentField(CommitInfo))
    smf_ops_center_commits = me.ListField(me.EmbeddedDocumentField(CommitInfo))

    created_on = me.DateTimeField(required=True, default=datetime.datetime.utcnow)
    meta = dict(collection='commit_info')

def init_connection():
    me.connect(db=DATABASE, host=MONGO_IP, port=27017)
