/**
 * ЗОНА ОТВЕТСТВЕННОСТИ: Frontend.
 * Задача: оживить страницу — общаться с сервером через fetch() и рисовать график через Chart.js.
 */

// Глобальные переменные (понадобятся, чтобы перерисовывать график и хранить список эталонов)
let chartInstance = null;
let referenceOils = [];


/**
 * Загружает список эталонных нефтей с сервера (GET /api/references)
 * и добавляет их как <option> внутрь <select id="presetSelect">.
 *
 * Вход: ничего.
 * Выход: заполненный выпадающий список на странице + сохранение массива в referenceOils.
 */
async function loadReferences() {
    // TODO: написать реализацию
}


/**
 * Обработчик выбора эталонной нефти из выпадающего списка.
 * Когда пользователь выбирает марку, нужно найти её в массиве referenceOils
 * и автоматически подставить её density, viscosity и sulfur в поля формы.
 *
 * Вход: event (событие 'change' у элемента #presetSelect).
 * Выход: заполненные поля формы.
 */
function handlePresetChange(event) {
    // TODO: написать реализацию
}


/**
 * Обработчик отправки формы (#oilForm).
 * 1. Отменить стандартную перезагрузку страницы (event.preventDefault()).
 * 2. Собрать числа из полей #density, #viscosity, #sulfur (через parseFloat).
 * 3. Отправить POST-запрос на /api/predict с JSON-телом.
 * 4. Получить ответ от сервера (curve, fractions, recommendation).
 * 5. Вызвать renderChart(), renderFractions() и обновить историю через loadHistory().
 *
 * Вход: event (событие 'submit' у формы).
 * Выход: обновленный график, текст и таблица истории на странице.
 */
async function handleFormSubmit(event) {
    // TODO: написать реализацию
}


/**
 * Рисует линейный график кривой разгонки на <canvas id="distillationChart"> с помощью Chart.js.
 * Подсказка: если chartInstance уже существует, сначала уничтожьте его через chartInstance.destroy().
 *
 * Вход: curve (объект вида {"100°C": 12.5, "180°C": 28.0, "240°C": 42.0, "350°C": 65.0}).
 * Выход: отрисованный график на странице.
 */
function renderChart(curve) {
    // TODO: написать реализацию
}


/**
 * Выводит список целевых фракций в #fractionsList и текст совета в #recommendationText.
 *
 * Вход:
 *   fractions (объект вида {"Бензиновая (до 180°C)": 28.0, ...})
 *   recommendation (строка текста)
 * Выход: обновленный HTML внутри блоков.
 */
function renderFractions(fractions, recommendation) {
    // TODO: написать реализацию
}


/**
 * Запрашивает последние расчеты с сервера (GET /api/history)
 * и вставляет строки <tr>...</tr> внутрь <tbody id="historyTableBody">.
 *
 * Вход: ничего.
 * Выход: заполненная таблица истории на странице.
 */
async function loadHistory() {
    // TODO: написать реализацию
}


// TODO: Повесить обработчики событий (addEventListener):
// - На загрузку страницы (DOMContentLoaded): вызвать loadReferences() и loadHistory().
// - На изменение #presetSelect: вызвать handlePresetChange.
// - На отправку #oilForm: вызвать handleFormSubmit.