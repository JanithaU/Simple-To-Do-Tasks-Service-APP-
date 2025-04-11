const API_URL = window.env.API_BASE_URL + "/tasks";
const taskContainer = document.getElementById("taskContainer");
const form = document.getElementById("taskForm");

async function fetchTasks() {
  try {
    const res = await fetch(API_URL);
    const tasks = await res.json();

    const limitedTasks = tasks.slice(0, 5);
    taskContainer.innerHTML = "";

    limitedTasks.forEach(task => {
      const li = document.createElement("li");

      const taskInfo = document.createElement("div");
      taskInfo.innerHTML = `
        <strong>${task.title}</strong><br>
        ${task.description}<br>
      `;

      const doneBtn = document.createElement("button");
      doneBtn.textContent = "Done";

      // Disable button if already marked as done
      if (task.status === "Done") {
        doneBtn.disabled = true;
        doneBtn.style.backgroundColor = "#ccc";
        doneBtn.textContent = "Completed";
      }

      doneBtn.onclick = async () => {
        try {
          const res = await fetch(`${API_URL}/${task.id}`, {
            method: "PUT",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify({ status: "Done" })
          });

          if (res.ok) {
            fetchTasks(); // Re-fetch to update UI
          } else {
            console.error("Failed to update task status");
          }
        } catch (err) {
          console.error("Error marking task as done:", err);
        }
      };

      li.appendChild(taskInfo);
      li.appendChild(doneBtn);
      taskContainer.appendChild(li);
    });
  } catch (err) {
    console.error("Failed to fetch tasks:", err);
  }
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const title = document.getElementById("title").value.trim();
  const description = document.getElementById("description").value.trim();

  if (!title || !description) return;

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, description })
    });

    if (res.ok) {
      form.reset();
      fetchTasks();
    } else {
      console.error("Error creating task");
    }
  } catch (err) {
    console.error("Failed to create task:", err);
  }
});

window.addEventListener("DOMContentLoaded", fetchTasks);
