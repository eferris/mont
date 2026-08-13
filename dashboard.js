
<div class="dashboard-grid">
  <!-- Left Column: Top Left Teachers with Students below -->
  <div class="sidebar">
    <div class="card">
      <label for="teacher-select">Teachers</label>
      <select id="teacher-select">
        <option value="">Select a Teacher...</option>
      </select>

      <label for="student-select">Students</label>
      <select id="student-select">
        <option value="">Select a Student...</option>
      </select>

      <button id="load-lessons-btn">Load Lessons</button>
    </div>
  </div>

  <!-- Right Main Area: Subjects & Lessons -->
  <div class="main-content">
    <div class="card">
      <label for="subject-select">Subjects</label>
      <select id="subject-select">
        <option value="">Select a Subject...</option>
      </select>

      <label for="lesson-select">Lessons</label>
      <select id="lesson-select">
        <option value="">Select a Lesson...</option>
      </select>

      <div id="lesson-content-display" class="lesson-display">
        <p><em>Select a student and click "Load Lessons" to display lesson details.</em></p>
      </div>
    </div>
  </div>
</div>

<script>
  // Mock Data Collections
  const mockTeachers = [
    { teacher_id: 1, name: "Prof. Davis" },
    { teacher_id: 2, name: "Dr. Martinez" }
  ];

  const mockSubjects = [
    { subject_id: 101, title: "Biology" },
    { subject_id: 102, title: "Geometry" },
    { subject_id: 103, title: "Music" }
  ];

  const mockStudents = [
    { student_id: 501, name: "Alice Smith" },
    { student_id: 502, name: "Bob Jones" }
  ];

  const mockLessons = [
    { lesson_id: 201, title: "Cell Structure Basics", content: "Overview of organelle functions." },
    { lesson_id: 202, title: "Pythagorean Theorem", content: "Applying a^2 + b^2 = c^2 in geometry." }
  ];

  // DOM Elements
  const teacherSelect = document.getElementById('teacher-select');
  const studentSelect = document.getElementById('student-select');
  const subjectSelect = document.getElementById('subject-select');
  const lessonSelect = document.getElementById('lesson-select');
  const loadLessonsBtn = document.getElementById('load-lessons-btn');
  const lessonDisplay = document.getElementById('lesson-content-display');

  // Generic helper function to populate <select> options
  function populateSelect(selectElement, items, valueKey, textKey) {
    items.forEach(item => {
      const option = document.createElement('option');
      option.value = item[valueKey];
      option.textContent = item[textKey];
      selectElement.appendChild(option);
    });
  }

  // 1. Explicitly load Teacher select element (and initial data)
  function loadTeacherSelectData() {
    populateSelect(teacherSelect, mockTeachers, 'teacher_id', 'name');
    populateSelect(studentSelect, mockStudents, 'student_id', 'name');
    populateSelect(subjectSelect, mockSubjects, 'subject_id', 'title');
  }

  // 2. Listener for Teacher element selection change
  teacherSelect.addEventListener('change', (event) => {
    const selectedTeacherId = event.target.value;
    console.log(`Teacher selected ID: ${selectedTeacherId}`);
    // Custom logic or API re-fetch can be triggered here on teacher change
  });

  // 3. Button Listener targeting Student selection to update Lesson content
  loadLessonsBtn.addEventListener('click', () => {
    const selectedStudentId = studentSelect.value;

    if (!selectedStudentId) {
      alert("Please select a student first.");
      return;
    }

    // Clear and populate lessons dropdown
    lessonSelect.innerHTML = '<option value="">Select a Lesson...</option>';
    populateSelect(lessonSelect, mockLessons, 'lesson_id', 'title');

    // Dynamically update the lesson content area for the chosen student
    const studentName = studentSelect.options[studentSelect.selectedIndex].text;
    lessonDisplay.innerHTML = `
      <strong>Assigned Lessons for ${studentName}:</strong>
      <ul>
        ${mockLessons.map(l => `<li><strong>${l.title}:</strong> ${l.content}</li>`).join('')}
      </ul>
    `;
  });

  // Initialize view
  loadTeacherSelectData();
</script>





// Define your screen templates/render functions
function renderLoginScreen() {
  return `
    <main id="app">
      <h1>Login</h1>
      <form id="login-form">
        <input type="text" placeholder="Username" required />
        <button type="submit">Log In</button>
      </form>
    </main>
  `;
}

function renderDashboardScreen(user) {
  return `
    <main id="app">
      <h1>Welcome, ${user}!</h1>
      <button id="logout-btn">Log Out</button>
    </main>
  `;
}

// Function to update the body/screen
function navigateTo(screenHtml) {
  // Option A: Direct innerHTML replacement on document.body
  document.body.innerHTML = screenHtml;
  
  // Re-attach event listeners required for the new screen
  attachScreenEvents();
}

// Example usage
navigateTo(renderLoginScreen());