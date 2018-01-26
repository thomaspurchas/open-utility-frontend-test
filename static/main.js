'use strict';
// Becausse JS has no useful string methods, we will add our own.
// https://stackoverflow.com/a/2648463
String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

function renderCalendar(displayType) {
    var WEEKS_TEMPLATE = $('#weeks-template').html();
    var WEEK_TEMPLATE = $('#week-template').html();
    var DAY_TEMPLATE = $('#day-template').html();
    var API = '/forcast/';
    var EMOJI_API = '/forcast/emoji/';

    var api_url = (displayType == 'emoji' ? EMOJI_API : API);

    var today = moment();
    
    // Moment.day() returns DoW with Sunday = 0
    // We need Sunday = 6
    var pastDaysThisWeek = (today.day() + 6) % 7;
    var futureDaysThisWeek = 6 - pastDaysThisWeek;
    var startDate = moment(today).day(0);

    var datesToNodes = {};

    var weeksNode = $(WEEKS_TEMPLATE);

    for (var currentWeek = 0; currentWeek <=4; currentWeek ++) {
        var weekStartDate = moment(startDate);
        weekStartDate.week(weekStartDate.week() + currentWeek);

        var weekNode = $(WEEK_TEMPLATE);

        for (var doW = 0; doW < 7; doW++) {
            var currentDate = moment(weekStartDate).day(doW + 1);

            var dayNode = $(DAY_TEMPLATE);

            if (currentDate.day() === 0 || currentDate.day() == 6) {
                dayNode.addClass('weekend');
            }

            if (currentDate.isBefore(today)) {
                dayNode.addClass('past');
            } else if (currentDate.isSame(today)) {
                dayNode.addClass('today');
            }

            if (currentDate.isAfter(today) && currentDate.date() == 1) {
                dayNode.find('header').text(currentDate.format('MMM D'));
            } else {
                dayNode.find('header').text(currentDate.format('D'));
            }
            
            if (displayType == 'emoji') {
                dayNode.find('.day-content').addClass('emoji');
            }

            datesToNodes[currentDate.format('YYYY/MM/DD')] = dayNode.find('.day-content');

            weekNode.append(dayNode);
        }

        weeksNode.append(weekNode);
    }

    $('.calendar .weeks').replaceWith(weeksNode);
    $('.calendar .header.today').text(today.format('MMMM YYYY'));

    var datesToGet = Object.keys(datesToNodes);

    $.post(api_url, JSON.stringify(datesToGet), "json")
        .done(function(data) {
            Object.keys(data).forEach(function(key) {
                datesToNodes[key].text(data[key]);
            });
        })
        .fail(function() {
            Object.keys(datesToNodes).forEach(function(key) {
                datesToNodes[key].text("So Error, Much Fail 😞");
            });
        });
}

function setup() {
    renderCalendar($('#displaySelector').val());

    $('#displaySelector').change(function() {
        renderCalendar($('#displaySelector').val());
    });
}

$(setup);