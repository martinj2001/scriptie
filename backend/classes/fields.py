from .field import Field
from .input_type import InputType
from typing import TypedDict

defaultMinChar = 200

fields = {
    '0.2.3b': {
        'name': Field(
            InputType.TEXT,
            True,
            100,
            10,
        ),
        'organization': Field(
            InputType.TEXT,
            True,
            100,
            10
        ),
        'department': Field(
            InputType.TEXT,
            True,
            500,
            25
        ),
        'description_short': Field(
            InputType.TEXT,
            True,
            500,
            100
        ),
        'type': Field(
            InputType.ALGO_TYPE,
            True,
            20,
            10
        ),
        'category': Field(
            InputType.TEXT,
            True,
            50,
            500
        ),
        'website': Field(
            InputType.URL,
            True,
            500,
            25
        ),
        'status': Field(
            InputType.STATUS,
            True,
            30,
            10
        ),
        'inzet.goal': Field(
            InputType.TEXT,
            True,
            5000,
            1000
        ),
        'inzet.impact': Field(
            InputType.TEXT,
            True,
            5000,
            1000
        ),
        'inzet.proportionality': Field(
            InputType.TEXT,
            True,
            5000,
            1000
        ),
        'inzet.decision_making_process': Field(
            InputType.TEXT,
            True,
            5000,
            1000
        ),
        'inzet.documentation': Field(
            InputType.URL,
            False,
            defaultMinChar,
            0
        ),
        'juridisch.competent_authority': Field(
            InputType.TEXT,
            True,
            100,
            20
        ),
        'juridisch.lawful_basis': [Field(
            InputType.TEXT,
            True,
            5000,
            1000
        ), Field(
            InputType.URL,
            True,
            150,
            25
        )],
        'juridisch.iama': Field(
            InputType.YESNO,
            True,
            3,
            2
        ),
        'juridisch.iama_description': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar,
            'juridisch.iama'
        ),
        'juridisch.dpia': Field(
            InputType.YESNO,
            False,
            3,
            2
        ),
        'juridisch.dpia_description': Field(
            InputType.TEXT,
            False,
            5000,
            defaultMinChar,
            'juridisch.dpia'
        ),
        'juridisch.objection_procedure': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar
        ),
        'metadata_algorithm.url': Field(
            InputType.URL,
            True,
            50,
            defaultMinChar
        ),
        'metadata_algorithm.contact_email': Field(
            InputType.EMAIL,
            True,
            100,
            10
        ),
        'metadata_algorithm.area': Field(
            InputType.TEXT,
            True,
            100,
            20
        ),
        'metadata_algorithm.lang': Field(
            InputType.LANGUAGE,
            True,
            100,
            10
        ),
        'metadata_algorithm.revision_date': Field(
            InputType.DATE,
            False,
            15,
            8
        ),
        'toepassing.description': Field(
            InputType.TEXT,
            False,
            5000,
            250
        ),
        'toepassing.application_url': Field(
            InputType.URL,
            True,
            150,
            20
        ),
        'toepassing.mprd': Field(
            InputType.YESNO,
            True,
            3,
            2
        ),
        'toepassing.source_data': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar
        ),
        'toepassing.methods_and_models': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar
        ),
        'toezicht.monitoring': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar
        ),
        'toezicht.human_intervention': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar
        ),
        'toezicht.risks': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar
        ),
        'toezicht.performance_standard': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar
        )},
    '0.3.1a': {
        'name': Field(
            InputType.TEXT,
            True,
            100,
            10,
        ),
        'organization': Field(
            InputType.TEXT,
            True,
            100,
            10
        ),
        'department': Field(
            InputType.TEXT,
            True,
            500,
            25
        ),
        'description_short': Field(
            InputType.TEXT,
            True,
            500,
            100
        ),
        'type': Field(
            InputType.ALGO_TYPE,
            True,
            20,
            10
        ),
        'category': Field(
            InputType.TEXT,
            True,
            50,
            500
        ),
        'website': Field(
            InputType.URL,
            True,
            500,
            25
        ),
        'status': Field(
            InputType.STATUS,
            True,
            30,
            10
        ),
        'goal': Field(
            InputType.TEXT,
            True,
            5000,
            1000
        ),
        'impact': Field(
            InputType.TEXT,
            True,
            5000,
            1000
        ),
        'proportionality': Field(
            InputType.TEXT,
            True,
            5000,
            1000
        ),
        'decision_making_process': Field(
            InputType.TEXT,
            True,
            5000,
            1000
        ),
        'documentation': Field(
            InputType.URL,
            False,
            defaultMinChar,
            0
        ),
        'competent_authority': Field(
            InputType.TEXT,
            True,
            100,
            20
        ),
        'lawful_basis': [Field(
            InputType.TEXT,
            True,
            5000,
            1000
        ), Field(
            InputType.URL,
            True,
            150,
            25
        )],
        'iama': Field(
            InputType.YESNO,
            True,
            3,
            2
        ),
        'iama_description': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar,
            'juridisch.iama'
        ),
        'dpia': Field(
            InputType.YESNO,
            False,
            3,
            2
        ),
        'dpia_description': Field(
            InputType.TEXT,
            False,
            5000,
            defaultMinChar,
            'juridisch.dpia'
        ),
        'objection_procedure': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar
        ),
        'standard_version': Field(
            InputType.TEXT,
            False,
            250,
            0,
        ),
        'url': Field(
            InputType.URL,
            True,
            50,
            defaultMinChar
        ),
        'contact_email': Field(
            InputType.EMAIL,
            True,
            100,
            10
        ),
        'area': Field(
            InputType.TEXT,
            True,
            100,
            20
        ),
        'lang': Field(
            InputType.LANGUAGE,
            True,
            100,
            10
        ),
        'revision_date': Field(
            InputType.DATE,
            False,
            15,
            8
        ),
        'description': Field(
            InputType.TEXT,
            False,
            5000,
            250
        ),
        'application_url': Field(
            InputType.URL,
            True,
            150,
            20
        ),
        'mprd': Field(
            InputType.YESNO,
            True,
            3,
            2
        ),
        'source_data': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar
        ),
        'methods_and_models': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar
        ),
        'monitoring': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar
        ),
        'human_intervention': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar
        ),
        'risks': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar
        ),
        'performance_standard': Field(
            InputType.TEXT,
            True,
            5000,
            defaultMinChar
        )
    }
}
