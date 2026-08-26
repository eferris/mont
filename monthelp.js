

// globals
  import { stateTeacher } from './state.js';
  import { stateStudent } from './state.js';
  import { stateSubject } from './state.js';
  import { stateLesson } from './state.js';
  import { myDisplay } from './state.js';


/**
 * Initializes the dropdowns, populates baseline options, attaches listeners,
 * and sets initial disabled/enabled states.
 */
export function initScreen() {
    // 1. Initial baseline population
    renderSelectOptions(stateTeacher.container, stateTeacher.getOptions(), 'teacher_id', 'name', '-- Select Teacher --');
    renderSelectOptions(stateStudent.container, stateStudent.getOptions(), 'student_id', 'name', '-- Select Student --');
    renderSelectOptions(stateSubject.container, stateSubject.getOptions(), 'subject_id', 'name', '-- Select Subject --');
    
//    clearSelect(stateStudent.container, '-- Select Student --');
    clearSelect(stateLesson.container, '-- Select Lesson --');

    // 2. Initial state configuration
    stateTeacher.container.disabled = false;
    stateSubject.container.disabled = false;
    stateStudent.container.disabled = true;
    stateLesson.container.disabled = true;

    // 3. Attach Event Listeners
    stateTeacher.container.addEventListener('change', onTeacherChange);
    stateStudent.container.addEventListener('change', onStudentChange);
    stateSubject.container.addEventListener('change', onSubjectChange);
}


/**
 * Event Handler: Teacher Change
 * Resets student selection, repopulates students for the selected teacher,
 * and cascades update to lesson state.
 */
function onTeacherChange() {

    let teacherId = stateTeacher.container.value;

    // Reset dependent student dropdown
    clearSelect(stateStudent.container, '-- Select Student --');

    if (teacherId !== '') {
        const allStudents = stateStudent.getOptions();
        const teacherStudents = allStudents.filter(student => 
            String(student.teacher_id) === String(teacherId)
        );

        renderSelectOptions(stateStudent.container, teacherStudents, 'student_id', 'name', '-- Select Student --');
        stateStudent.container.disabled = false;
    } else {
        // Teacher cleared to default
        stateStudent.container.disabled = true;
    }

    // Recalculate Lesson dropdown state and options
    updateLessonState();
}

/**
 * Event Handler: Student Change
 */
function onStudentChange() {
    updateLessonState();
}

/**
 * Event Handler: Subject Change
 */
function onSubjectChange() {
    updateLessonState();
}


/**
 * Helper subroutine to filter Lesson options and toggle enabled/disabled state
 * based on the current selections of Student and Subject.
 */
export function updateLessonState() {
    const studentVal = stateStudent.container.value;
    const subjectVal = stateSubject.container.value;
    const TeacherVal = stateTeacher.container.value;
    const subjectIndex = stateSubject.container.selectedIndex;
    const studentIndex = stateStudent.container.selectedIndex;
    const student_name = stateStudent.container.options[stateStudent.container.selectedIndex].innerHTML;
    const subject_name = stateSubject.container.options[stateSubject.container.selectedIndex].innerHTML;
   
    const allLessons = stateLesson.getOptions();

    myDisplay.typeName = '';
    myDisplay.selectedName = '';

    // 1. Reset current Lesson selection and clear options
    clearSelect(stateLesson.container, '-- Select Lesson --');

    let filteredLessons = [];
    let newContent = []

    // 2. Evaluate selection combinations
    if (studentVal !== '' && subjectVal !== '') {
        // Case 1: Both Student and Subject are selected
        filteredLessons = allLessons.filter(lesson => 
            String(lesson.student_id) === String(studentVal) &&
            String(lesson.subject_id) === String(subjectVal)
        );

//        student_name = stateStudent[studentIndex];
//        subject_name = stateSubject.data[subjectIndex];

        if (filteredLessons.length === 0) {

            myDisplay.typeName = 'No Lessons for ' + student_name + ' and ' + subject_name;
            newContent = myDisplay.oldContent;
        }
        else
        {
            renderSelectOptions(stateLesson.container, filteredLessons, 'lesson_id', 'name', '-- Select Lesson --');
            stateLesson.container.disabled = false;

            myDisplay.typeName =  subject_name + ' ';  
            myDisplay.selectedName = 
            'Lessons for ' + student_name;  

            newContent = stateLesson.container.innerHTML.replace( '-- Select Lesson --', '-- Completed --')
        }

    } else if (subjectVal !== '') {   
        // Case 2: Only Subject is selected
        filteredLessons = allLessons.filter(lesson => 
            String(lesson.subject_id) === String(subjectVal)
        );

//        renderSelectOptions(stateLesson.container, filteredLessons, 'lesson_id', 'name', '-- Select Lesson --');
        stateLesson.container.disabled = false;
        newContent = myDisplay.oldContent;
        myDisplay.typeName = "Curriculum For "
        myDisplay.selectedName = subject_name;
        myDisplay.container.innerHTML = '';

    } else if (studentVal !== '') {
        // Case 3: Only Student is selected
        filteredLessons = allLessons.filter(lesson => 
            String(lesson.student_id) === String(studentVal)
        );

        if (filteredLessons.length === 0) {
            myDisplay.typeName = 'No Lessons for ' + student_name;
            newContent = myDisplay.oldContent;
        } 
        else
        {
            renderSelectOptions(stateLesson.container, filteredLessons, 'lesson_id', 'name', '-- Select Lesson --');
            stateLesson.container.disabled = false;
            myDisplay.typeName = 'Lessons for ' + student_name;
            newContent = stateLesson.container.innerHTML.replace( '-- Select Lesson --', 'Completed')
        }

    } else {
        // Case 4: Neither Student nor Subject is selected
        stateLesson.container.disabled = true;
        myDisplay.typeName = 'Make Selection(s)';
        myDisplay.selectedName = '';
        newContent = myDisplay.oldContent;
    }

    myDisplay.container.innerHTML = `
        <strong>${myDisplay.typeName} ${myDisplay.selectedName}</strong>
            <p><em>${newContent}</em></p>

        `;    
}


/**
 * Clears and repopulates a <select> dropdown element with a default placeholder.
 * @param {HTMLSelectElement} selectElement - The select element to populate.
 * @param {Array} items - Array of data objects.
 * @param {string} idKey - Key name for the value attribute (e.g., 'teacher_id').
 * @param {string} labelKey - Key name for visible text (e.g., 'name', 'title').
 * @param {string} defaultText - Placeholder text for the default empty option.
 */
export function renderSelectOptions(selectElement, items, idKey, labelKey = 'name', defaultText = '-- Select --') {
    selectElement.innerHTML = '';

    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.textContent = defaultText;
    selectElement.appendChild(defaultOption);

    items.forEach(item => {
        const option = document.createElement('option');
        option.value = item[idKey];
        option.textContent = item[labelKey] || item.title || item[idKey];
        selectElement.appendChild(option);
    });

    selectElement.value = '';
}

/**
 * Resets a select element to default placeholder and clears options.
 */
function clearSelect(selectElement, defaultText = '-- Select --') {
    selectElement.innerHTML = `<option value="">${defaultText}</option>`;
    selectElement.value = '';
}