document.addEventListener("DOMContentLoaded", function() {
    const inputs = document.querySelectorAll("input[type='number']");

    function calculateSum(groupPrefix, sumInputName) {
        let sum = 0;
        inputs.forEach(input => {
            if (input.name.startsWith(groupPrefix) && input.name !== sumInputName) {
                sum += parseFloat(input.value) || 0;
            }
        });
        document.querySelector(`input[name='${sumInputName}']`).value = sum;
    }

    function updateIndicator1600() {
        const indicator1100 = parseFloat(document.querySelector("input[name='indicator_1100']").value) || 0;
        const indicator1200 = parseFloat(document.querySelector("input[name='indicator_1200']").value) || 0;
        document.querySelector("input[name='indicator_1600']").value = indicator1100 + indicator1200;
    }

    function updateIndicator1700() {
        const indicator1300 = parseFloat(document.querySelector("input[name='indicator_1300']").value) || 0;
        const indicator1400 = parseFloat(document.querySelector("input[name='indicator_1400']").value) || 0;
        const indicator1500 = parseFloat(document.querySelector("input[name='indicator_1500']").value) || 0;
        document.querySelector("input[name='indicator_1700']").value = indicator1300 + indicator1400 + indicator1500;
    }

    inputs.forEach(input => {
        if (input.name.startsWith('indicator_11') && input.name !== 'indicator_1100') {
            input.addEventListener('input', function() {
                calculateSum('indicator_11', 'indicator_1100');
                updateIndicator1600();
            });
        }
        if (input.name.startsWith('indicator_12') && input.name !== 'indicator_1200') {
            input.addEventListener('input', function() {
                calculateSum('indicator_12', 'indicator_1200');
                updateIndicator1600();
            });
        }
        if (input.name.startsWith('indicator_13') && input.name !== 'indicator_1300') {
            input.addEventListener('input', function() {
                calculateSum('indicator_13', 'indicator_1300');
                updateIndicator1700();
            });
        }
        if (input.name.startsWith('indicator_14') && input.name !== 'indicator_1400') {
            input.addEventListener('input', function() {
                calculateSum('indicator_14', 'indicator_1400');
                updateIndicator1700();
            });
        }
        if (input.name.startsWith('indicator_15') && input.name !== 'indicator_1500') {
            input.addEventListener('input', function() {
                calculateSum('indicator_15', 'indicator_1500');
                updateIndicator1700();
            });
        }
    });
});

function readFile() {
    var fileInput = document.getElementById('formFile');
    if (fileInput.files.length === 0) {
        alert("Выберите файл Excel для загрузки.");
        return;
    }

    var file = fileInput.files[0];
    var reader = new FileReader();

    reader.onload = function(event) {
        var data = event.target.result;
        var workbook = XLSX.read(data, { type: 'array' });
        var firstSheetName = workbook.SheetNames[0];
        var firstSheet = workbook.Sheets[firstSheetName];

        // Пример чтения данных из ячеек и заполнения полей ввода с проверкой на существование ячейки
        var startRow1 = 1; // Начальная строка для первого диапазона (1110 - 1190)
var endRow1 = 9; // Конечная строка для первого диапазона

for (var i = startRow1; i <= endRow1; i++) {
    var cellAddress1 = 'A' + i;
    if (firstSheet[cellAddress1] !== undefined && firstSheet[cellAddress1].v !== undefined) {
        var cellValue1 = firstSheet[cellAddress1].v;
        var indicatorId1 = 1110 + (i - startRow1) * 10; // Вычисляем идентификатор индикатора на основе текущей строки
        document.querySelector('input[name="indicator_' + indicatorId1 + '"]').value = cellValue1;
    } else {
        console.error("Ячейка " + cellAddress1 + " не найдена или не содержит значения.");
    }
}

var startRow2 = 10; // Начальная строка для второго диапазона (1210 - 1260)
var endRow2 = 15; // Конечная строка для второго диапазона

for (var j = startRow2; j <= endRow2; j++) {
    var cellAddress2 = 'A' + j;
    if (firstSheet[cellAddress2] !== undefined && firstSheet[cellAddress2].v !== undefined) {
        var cellValue2 = firstSheet[cellAddress2].v;
        var indicatorId2 = 1210 + (j - startRow2) * 10; // Вычисляем идентификатор индикатора на основе текущей строки
        document.querySelector('input[name="indicator_' + indicatorId2 + '"]').value = cellValue2;
    } else {
        console.error("Ячейка " + cellAddress2 + " не найдена или не содержит значения.");
    }
}

var startRow3 = 16; // Начальная строка для третьего диапазона (1210 - 1260)
var endRow3 = 22; // Конечная строка для третьего диапазона

for (var j = startRow3; j <= endRow3; j++) {
    var cellAddress3 = 'A' + j;
    if (firstSheet[cellAddress3] !== undefined && firstSheet[cellAddress3].v !== undefined) {
        var cellValue3 = firstSheet[cellAddress3].v;
        var indicatorId3 = 1310 + (j - startRow3) * 10; // Вычисляем идентификатор индикатора на основе текущей строки

        // Проверяем, существует ли индикатор с этим идентификатором
        var indicatorElement = document.querySelector('input[name="indicator_' + indicatorId3 + '"]');
        if (indicatorElement !== null) {
            indicatorElement.value = cellValue3;
        } else {
            console.error("Индикатор с идентификатором " + indicatorId3 + " не найден.");
        }
    } else {
        console.error("Ячейка " + cellAddress3 + " не найдена или не содержит значения.");
    }
}
var startRow4 = 23; // Начальная строка для третьего диапазона (1210 - 1260)
var endRow4 = 27; // Конечная строка для третьего диапазона

for (var j = startRow4; j <= endRow4; j++) {
    var cellAddress4 = 'A' + j;
    if (firstSheet[cellAddress4] !== undefined && firstSheet[cellAddress4].v !== undefined) {
        var cellValue4 = firstSheet[cellAddress4].v;
        var indicatorId4 = 1410 + (j - startRow4) * 10; // Вычисляем идентификатор индикатора на основе текущей строки

        // Проверяем, существует ли индикатор с этим идентификатором
        var indicatorElement = document.querySelector('input[name="indicator_' + indicatorId4 + '"]');
        if (indicatorElement !== null) {
            indicatorElement.value = cellValue4;
        } else {
            console.error("Индикатор с идентификатором " + indicatorId4 + " не найден.");
        }
    } else {
        console.error("Ячейка " + cellAddress4 + " не найдена или не содержит значения.");
    }
}
var startRow5 = 28; // Начальная строка для третьего диапазона (1210 - 1260)
var endRow5 = 32; // Конечная строка для третьего диапазона

for (var j = startRow5; j <= endRow5; j++) {
    var cellAddress5 = 'A' + j;
    if (firstSheet[cellAddress5] !== undefined && firstSheet[cellAddress5].v !== undefined) {
        var cellValue5 = firstSheet[cellAddress5].v;
        var indicatorId5 = 1510 + (j - startRow5) * 10; // Вычисляем идентификатор индикатора на основе текущей строки

        // Проверяем, существует ли индикатор с этим идентификатором
        var indicatorElement = document.querySelector('input[name="indicator_' + indicatorId5 + '"]');
        if (indicatorElement !== null) {
            indicatorElement.value = cellValue5;
        } else {
            console.error("Индикатор с идентификатором " + indicatorId5 + " не найден.");
        }
    } else {
        console.error("Ячейка " + cellAddress5 + " не найдена или не содержит значения.");
    }
}

    };

    reader.readAsArrayBuffer(file);
}
