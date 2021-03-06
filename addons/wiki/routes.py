"""
Routes associated with the wiki page
"""

from framework.routing import Rule, json_renderer
from website.routes import OsfWebRenderer

from . import views

TEMPLATE_DIR = './addons/wiki/templates/'

settings_routes = {
    'rules': [],
    'prefix': '/api/v1',
}

# NOTE: <wname> refers to a wiki page's key, e.g. 'Home'
page_routes = {

    'rules': [

        # Home (Base) | GET
        Rule(
            [
                '/project/<pid>/wiki/',
                '/project/<pid>/node/<nid>/wiki/',
            ],
            'get',
            views.project_wiki_home,
            OsfWebRenderer('edit.mako', trust=False, template_dir=TEMPLATE_DIR)
        ),

        # View (Id) | GET
        Rule(
            [
                '/project/<pid>/wiki/id/<wid>/',
                '/project/<pid>/node/<nid>/wiki/id/<wid>/',
            ],
            'get',
            views.project_wiki_id_page,
            OsfWebRenderer('edit.mako', trust=False, template_dir=TEMPLATE_DIR)
        ),

        # Wiki | GET
        Rule(
            [
                '/project/<pid>/wiki/<wname>/',
                '/project/<pid>/node/<nid>/wiki/<wname>/',
            ],
            'get',
            views.project_wiki_view,
            OsfWebRenderer('edit.mako', trust=False, template_dir=TEMPLATE_DIR)
        ),

        # Edit | GET (legacy url, trigger redirect)
        Rule(
            [
                '/project/<pid>/wiki/<wname>/edit/',
                '/project/<pid>/node/<nid>/wiki/<wname>/edit/',
            ],
            'get',
            views.project_wiki_edit,
            OsfWebRenderer('edit.mako', trust=False, template_dir=TEMPLATE_DIR)
        ),

        # Compare | GET (legacy url, trigger redirect)
        Rule(
            [
                '/project/<pid>/wiki/<wname>/compare/<int:wver>/',
                '/project/<pid>/node/<nid>/wiki/<wname>/compare/<int:wver>/',
            ],
            'get',
            views.project_wiki_compare,
            OsfWebRenderer('edit.mako', trust=False, template_dir=TEMPLATE_DIR)
        ),

        # Edit | POST
        Rule(
            [
                '/project/<pid>/wiki/<wname>/',
                '/project/<pid>/node/<nid>/wiki/<wname>/',
            ],
            'post',
            views.project_wiki_edit_post,
            OsfWebRenderer('edit.mako', trust=False, template_dir=TEMPLATE_DIR)
        ),
    ]
}

api_routes = {

    'rules': [

        # Home (Base) : GET
        Rule([
            '/project/<pid>/wiki/',
            '/project/<pid>/node/<nid>/wiki/',
        ], 'get', views.project_wiki_home, json_renderer),

        # Draft : GET
        Rule([
            '/project/<pid>/wiki/<wname>/draft/',
            '/project/<pid>/node/<nid>/wiki/<wname>/draft/',
        ], 'get', views.wiki_page_draft, json_renderer),

        # Content : GET
        # <wver> refers to a wiki page's version number
        Rule([
            '/project/<pid>/wiki/<wname>/content/',
            '/project/<pid>/node/<nid>/wiki/<wname>/content/',
            '/project/<pid>/wiki/<wname>/content/<wver>/',
            '/project/<pid>/node/<nid>/wiki/<wname>/content/<wver>/',
        ], 'get', views.wiki_page_content, json_renderer),

        # Validate | GET
        Rule([
            '/project/<pid>/wiki/<wname>/validate/',
            '/project/<pid>/node/<nid>/wiki/<wname>/validate/',
        ], 'get', views.project_wiki_validate_name, json_renderer),

        # Edit | POST
        Rule([
            '/project/<pid>/wiki/<wname>/edit/',
            '/project/<pid>/node/<nid>/wiki/<wname>/edit/',
        ], 'post', views.project_wiki_edit_post, json_renderer),

        # Rename : PUT
        Rule([
            '/project/<pid>/wiki/<wname>/rename/',
            '/project/<pid>/node/<nid>/wiki/<wname>/rename/',
        ], 'put', views.project_wiki_rename, json_renderer),

        # Delete : DELETE
        Rule([
            '/project/<pid>/wiki/<wname>/',
            '/project/<pid>/node/<nid>/wiki/<wname>/',
        ], 'delete', views.project_wiki_delete, json_renderer),

        # Change Wiki Settings | PUT
        Rule([
            '/project/<pid>/wiki/settings/',
            '/project/<pid>/node/<nid>/wiki/settings/',
        ], 'put', views.edit_wiki_settings, json_renderer),

        #Permissions Info for Settings Page | GET
        Rule(
            [
                '/project/<pid>/wiki/settings/',
                '/project/<pid>/node/<nid>/wiki/settings/'
            ],
            'get',
            views.get_node_wiki_permissions,
            json_renderer,
        ),

        # Wiki Menu : GET
        Rule([
            '/project/<pid>/wiki/<wname>/grid/',
            '/project/<pid>/node/<nid>/wiki/<wname>/grid/'
        ], 'get', views.project_wiki_grid_data, json_renderer),

    ],

    'prefix': '/api/v1',

}
