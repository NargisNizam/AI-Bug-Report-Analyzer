const descriptionInput = document.getElementById("bugDescription");
const analyzeButton = document.getElementById("analyzeButton");
const buttonText = document.getElementById("buttonText");
const statusText = document.getElementById("status");
const resultSection = document.querySelector(".results-card");
const emptyState = document.getElementById("emptyState");
const formattedReport = document.getElementById("formattedReport");
const copyButton = document.getElementById("copyButton");
const charCount = document.getElementById("charCount");

const detailFields = {
  title: document.getElementById("detailTitle"),
  affected_feature: document.getElementById("detailFeature"),
  issue_summary: document.getElementById("detailSummary"),
  severity: document.getElementById("detailSeverity"),
  possible_causes: document.getElementById("detailCauses")
};

descriptionInput.addEventListener("input", () => {
  charCount.textContent = `${descriptionInput.value.length} / 1000`;
});

function showValue(element, value) {
  element.classList.remove("muted");
  element.textContent = value || "Not available";
}

function setSeverity(value) {
  const element = detailFields.severity;
  element.replaceChildren();
  element.classList.remove("muted");
  const badge = document.createElement("span");
  const normalized = String(value || "Medium").toLowerCase();
  badge.className = `severity-badge severity-${["critical", "high", "medium", "low"].includes(normalized) ? normalized : "medium"}`;
  badge.textContent = value || "Medium";
  element.appendChild(badge);
}

function switchTab(tabName) {
  document.querySelectorAll(".tab").forEach(tab => {
    tab.classList.toggle("active", tab.dataset.tab === tabName);
  });
  if (tabName === "severity") {
    document.querySelector(".severity-row").scrollIntoView({ behavior: "smooth", block: "nearest" });
  } else if (tabName === "causes") {
    detailFields.possible_causes.scrollIntoView({ behavior: "smooth", block: "nearest" });
  } else if (tabName === "report") {
    document.querySelector(".report-panel").scrollIntoView({ behavior: "smooth", block: "nearest" });
  } else {
    document.querySelector(".detail-panel").scrollIntoView({ behavior: "smooth", block: "nearest" });
  }
}
document.querySelectorAll(".tab").forEach(tab => {
  tab.addEventListener("click", () => switchTab(tab.dataset.tab));
});

analyzeButton.addEventListener("click", async () => {
  const description = descriptionInput.value.trim();

  if (description.length < 10) {
    statusText.textContent = "Please enter a bug description of at least 10 characters.";
    descriptionInput.focus();
    return;
  }

  analyzeButton.disabled = true;
  buttonText.textContent = "Analyzing...";
  statusText.textContent = "Gemini is analyzing your bug. This may take a few seconds.";
  emptyState.hidden = true;

  try {
    const response = await fetch("/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ description })
    });

    const data = await response.json();
    if (!response.ok) {
      throw new Error(typeof data.detail === "string" ? data.detail : JSON.stringify(data.detail || data));
    }

    const details = data.details || {};
    showValue(detailFields.title, details.title);
    showValue(detailFields.affected_feature, details.affected_feature);
    showValue(detailFields.issue_summary, details.issue_summary);
    setSeverity(details.severity);
    const causes = Array.isArray(details.possible_causes) ? details.possible_causes.join(" • ") : details.possible_causes;
    showValue(detailFields.possible_causes, causes);
    formattedReport.textContent = data.report || "No formatted report was returned.";
    statusText.textContent = "Report generated successfully.";
    switchTab("analysis");
  } catch (error) {
    emptyState.hidden = false;
    statusText.textContent = `Analysis failed: ${error.message}`;
  } finally {
    analyzeButton.disabled = false;
    buttonText.textContent = "Analyze Bug";
  }
});

copyButton.addEventListener("click", async () => {
  const text = formattedReport.textContent.trim();
  if (!text || text.includes("Your formatted report will appear here")) {
    statusText.textContent = "Generate a report before copying it.";
    return;
  }
  try {
    await navigator.clipboard.writeText(text);
    statusText.textContent = "Report copied to clipboard.";
  } catch {
    statusText.textContent = "Clipboard access was blocked. Select the report text and copy it manually.";
  }
});
