/**
 * Builds full page project browser
 */
'use strict';

var Treebeard = require('treebeard');   // Uses treebeard, installed as plugin
var $ = require('jquery');  // jQuery
var m = require('mithril'); // exposes mithril methods, useful for redraw etc.
var ProjectOrganizer = require('js/projectorganizer').ProjectOrganizer;


/**
 *  Options for fileBrowser
 */
var defaults = {
    wrapper : '#fileBrowser',  // Default ID for wrapping empty div, all contents will be filled in.
    tboptions : {},
    fullWidth : true
};

/**
 * Initialize File Browser. Prepeares an option object within FileBrowser
 * @constructor
 */
var FileBrowser = {
    controller : function (args) {
        var self = this;
        self.data = m.prop([]);

        self.breadcrumbs = [
            { label : 'First', href : '/first'},
            { label : 'Second', href : '/second'},
            { label : 'Third', href : '/third'}
        ];
        self.collections = [
            { id:1, label : 'Dashboard', href : '#'},
            { id:2, label : 'All My Registrations', href : '#'},
            { id:3, label : 'All My Projects', href : '#'},
            { id:4, label : 'Another Collection', href : '#'}
        ];

        self.renderCollections = function _renderDo(){
            if (self.data().data){
                self.data().data.map(function(item){
                    console.log(item.category);
                });
            }
        };

        self.poOptions = {
            placement : 'dashboard',
            divID: 'projectOrganizer',
            filesData: args.data,
            multiselect : true
        };

    },
    view : function (ctrl) {
        return m('', [
            m.component(Breadcrumbs, { data : ctrl.breadcrumbs } ),
            m('.fb-sidebar', [
                m.component(Collections, {list : ctrl.collections, selected : 1 } ),
                m.component(Filters)
            ]),
            m('.fb-main', m.component(ProjectOrganizer, { options : ctrl.poOptions })),
            m('.fb-infobar', m.component(Information))
        ]);
    }
};

/**
 * Collections Module.
 * @constructor
 */
var Collections  = {
    controller : function (data) {
        this.list = data.list|| [];
        this.selected = data.selected;
    },
    view : function (ctrl) {
        var selectedCSS;
        return m('.fb-collections', m('ul', [
            ctrl.list.map(function(item, index, array){
                selectedCSS = item.id === ctrl.selected ? '.active' : '';
                if (index === array.length-1){
                    return m('li' + selectedCSS,  item.label);
                }
                return m('li' + selectedCSS,
                    m('a', { href : item.href},  item.label)
                );
            })
        ]));
    }
};

/**
 * Breadcrumbs Module.
 * @constructor
 */
var Breadcrumbs = {
    controller : function (data) {
        this.data = data ? data.data : [];
    },
    view : function (ctrl) {
        return m('.fb-breadcrumbs', m('ul', [
            ctrl.data.map(function(item, index, array){
                if(index === array.length-1){
                    return m('li',  item.label);
                }
                return m('li',
                    m('a', { href : item.href},  item.label),
                    m('i.fa.fa-chevron-right')
                );
            })
        ]));
    }
};


/**
 * Filters Module.
 * @constructor
 */
var Filters = {
    controller : function (args) {

    },
    view : function (ctrl) {
        return m('.fb-filters', 'Filters');
    }
};


/**
 * Project Organizer Module.
 * @constructor
 */


/**
 * Information Module.
 * @constructor
 */
var Information = {
    controller : function (args) {

    },
    view : function (ctrl) {
        return m('.fb-information', 'Information');
    }
};



module.exports = FileBrowser;