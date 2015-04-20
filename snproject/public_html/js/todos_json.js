/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

function get_todos() {
    return JSON.parse(JSON.stringify([
        {
            id: 1,
            title: 'Flug nach Athen buchen',
            deadline: '2015-04-26T15:00:00',
            finished: 40
        },
        {
            id: 2,
            title: 'Kaffee trinken',
            deadline: '2015-04-22T15:00:00',
            finished: 50
        },
        {
            id: 3,
            title: 'Aufgabe 1 abgeben',
            deadline: '2015-04-21T15:00:00',
            finished: 10
        },
        {
            id: 4,
            title: 'Zeitfenster buchen',
            deadline: '2015-04-30T15:00:00',
            finished: 15
        },
        {
            id: 5,
            title: 'Tabak kaufen',
            deadline: '2015-04-30T15:00:00',
            finished: 70
        },
        {
            id: 6,
            title: 'Nicht aufhören zu rauchen',
            deadline: '2015-04-30T15:00:00',
            finished: 90
        },
        {
            id: 7,
            title: 'Eichhörnchen füttern',
            deadline: '2015-04-29T15:00:00',
            finished: 30
        },
        {
            id: 8,
            title: 'Auto waschen',
            deadline: '2015-04-01T15:00:00',
            finished: 40
        }
    ]));
}