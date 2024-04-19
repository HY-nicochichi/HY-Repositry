const subject = document.getElementById('dropdown');
const listNo = document.getElementById('listNo');
const starttime = document.getElementById('starttime');
const endtime = document.getElementById('endtime');

window.onload = function () {
    var now = new Date();
    var year = now.getFullYear();
    var month = now.getMonth() + 1;
    var day = now.getDate();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var toTwoDigits = function (num, digit) {
        num += '';
        if (num.length < digit) {
          num = '0' + num;
        };
        return num;
    };
    var yearStr = toTwoDigits(year, 4);
    var monthStr = toTwoDigits(month, 2);
    var dayStr = toTwoDigits(day, 2);
    var hoursStr = toTwoDigits(hours, 2);
    var minutesStr = toTwoDigits(minutes, 2);
    var current_time_Str = yearStr + "-" + monthStr + "-" + dayStr + "T" + hoursStr + ":" + minutesStr;
    starttime.min = current_time_Str;
    endtime.min = starttime.value;
};

starttime.addEventListener('change', () => {
    var now = new Date();
    var year = now.getFullYear();
    var month = now.getMonth() + 1;
    var day = now.getDate();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var toTwoDigits = function (num, digit) {
        num += '';
        if (num.length < digit) {
          num = '0' + num;
        };
        return num;
    };
    var yearStr = toTwoDigits(year, 4);
    var monthStr = toTwoDigits(month, 2);
    var dayStr = toTwoDigits(day, 2);
    var hoursStr = toTwoDigits(hours, 2);
    var minutesStr = toTwoDigits(minutes, 2);
    var current_time_Str = yearStr + "-" + monthStr + "-" + dayStr + "T" + hoursStr + ":" + minutesStr;
    starttime.min = current_time_Str;
    endtime.min = starttime.value;
});

subject.addEventListener('change', () => {
    if(subject.value=="english") {
        listNo.max = "3";
    }
    else {
        listNo.max = "2";
    };
});
