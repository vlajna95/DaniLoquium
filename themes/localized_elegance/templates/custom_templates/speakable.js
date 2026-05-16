$(document).ready(function() {
if (!("speechSynthesis" in window)) return;
const voiceSelect = $("#voiceSelect");
const speakableElements = $(".{{ SPEAKABLE_TEXT_DEFAULT_CLASS }}");
const defaultLanguage = "{{ SPEAKABLE_TEXT_DEFAULT_LANGUAGE }}";
const defaultVoices = {{ SPEAKABLE_TEXT_DEFAULT_VOICES|tojson }};
var voiceDefaults = defaultVoices[defaultLanguage] || Object.keys(defaultVoices).find(lang => defaultLanguage.startsWith(lang) || lang.startsWith(defaultLanguage));
var voices = [];
var voiceSpecified = localStorage.getItem("preferredVoice") || null;

// load voices and populate the dropdown
function loadVoices() {
voices = speechSynthesis.getVoices();
if (voices.length === 0) {
setTimeout(loadVoices, 100);
return;
}
var langBase = defaultLanguage.split("_")[0].split("-")[0];
var filteredVoices = voices.filter(voice => voice.lang === defaultLanguage || voice.lang.startsWith(langBase)).sort((a, b) => a.name.localeCompare(b.name));
voiceSelect.empty();
filteredVoices.forEach(voice => {
$("<option>").val(voice.name).attr({ "data-lang": voice.lang, "data-name": voice.name }).text(voice.name.replace("Microsoft ", "")).appendTo(voiceSelect);
});
var theVoice = voiceSpecified || voices.find(v => voiceDefaults.includes(v.name)) || voiceSelect.children().first().val();
// logText(text="theVoice: " + theVoice);
voiceSelect.val(theVoice) || voiceSelect.children().first().val();
}
if (speechSynthesis.onvoiceschanged !== undefined) {
speechSynthesis.onvoiceschanged = loadVoices;
}

// handle click on speakable elements
speakableElements.on("click", function() {
var text = $(this).data("text") || $(this).text();
var utterance = new SpeechSynthesisUtterance(text);
var language = $(this).attr("lang") || defaultLanguage;
var voice = null;
// determine the appropriate voice
voiceSpecified = $(this).data("voice") || voiceSelect.val() || localStorage.getItem("preferredVoice");
localStorage.setItem("preferredVoice", voiceSpecified);
voice = voices.find(v => v.name === voiceSpecified);
if (!voice) {
if (voiceDefaults) {
voice = voices.find(v => voiceDefaults.includes(v.name));
}
}
if (voice) {
utterance.voice = voice;
}
utterance.lang = language;
if (utterance.voice != null) {
if (utterance.voice.name.startsWith("Microsoft") || utterance.voice.name.startsWith("Google")) {
utterance.rate = 1.1;
}
else {
utterance.rate = 1.1;
}
if (utterance.voice.name.startsWith("VE")) {
utterance.volume = 0.7;
}
else {
utterance.volume = 1.0;
}
}
speechSynthesis.cancel();
speechSynthesis.speak(utterance);
});
});

/*
$(document).ready(function() {
if("speechSynthesis" in window) {
var voices = [];
var voiceNames = [];
var speakableElements = $(".{{ SPEAKABLE_TEXT_DEFAULT_CLASS }}");
speechSynthesis.onvoiceschanged = function() {
voices = speechSynthesis.getVoices();
var voiceDropdown = document.getElementById("voiceDropdown");
if(voices.length > 0 && speakableElements.length > 0 && "{{ SPEAKABLE_TEXT_VOICE_CHANGER }}" && "{{ SPEAKABLE_TEXT_VOICE_CHANGER }}" !== "False") {
voiceDropdown.style.display = "block";
}
voices.forEach(function(voice, index) {
voiceNames.push(voice.name);
var option = document.createElement("option");
option.value = index;
option.textContent = voice.name;
voiceDropdown.appendChild(option);
}); // end of voices.forEach
if("{{ SPEAKABLE_TEXT_VOICE_CHANGER }}" && "{{ SPEAKABLE_TEXT_VOICE_CHANGER }}" !== "False") {
var defaultVoice = voices.find(function(voice) {
return voice.name === "{{ SPEAKABLE_TEXT_DEFAULT_VOICE }}";
});
if(!defaultVoice) {
defaultVoice = voices.find(function(voice) {
return voice.lang.startsWith("{{ SPEAKABLE_TEXT_DEFAULT_LANGUAGE }}");
});
}
var defaultVoiceIndex = 0;
if(defaultVoice) {
defaultVoiceIndex = voices.indexOf(defaultVoice);
}
voiceDropdown.selectedIndex = defaultVoiceIndex;
voiceDropdown.focus();
} // end of if SPEAKABLE_TEXT_VOICE_CHANGER
}; // end of onvoiceschanged
// get all elements with the class "{{ SPEAKABLE_TEXT_DEFAULT_CLASS }}" class
speakableElements.each(function() {
// add click event listeners to each speakable element
$(this).on("click", function() {
var utterance = new SpeechSynthesisUtterance($(this).text());
if("{{ SPEAKABLE_TEXT_VOICE_CHANGER }}" && "{{ SPEAKABLE_TEXT_VOICE_CHANGER }}" !== "False") {
var selectedVoice = $("#voiceDropdown option:selected").text();
utterance.voice = voices.find(function(voice) {
return voice.name === selectedVoice;
});
}
else {
if("{{ SPEAKABLE_TEXT_DEFAULT_VOICE }}" && "{{ SPEAKABLE_TEXT_DEFAULT_VOICE }}" in voiceNames) {
var defaultVoice = voices.find(function(voice) {
return voice.name === "{{ SPEAKABLE_TEXT_DEFAULT_VOICE }}";
});
if(defaultVoice) {
utterance.voice = defaultVoice;
}
else if($(this).attr("lang")) {
utterance.lang = $(this).attr("lang");
}
else {
utterance.lang = "{{ SPEAKABLE_TEXT_DEFAULT_LANGUAGE }}";
}
}
else if($(this).attr("lang")) {
utterance.lang = $(this).attr("lang");
}
else {
utterance.lang = "{{ SPEAKABLE_TEXT_DEFAULT_LANGUAGE }}";
}
}
speechSynthesis.speak(utterance);
}); // end of click listener definition
}); // end of speakableElements.each
} // end of if("speechSynthesis" in window)
});
*/
