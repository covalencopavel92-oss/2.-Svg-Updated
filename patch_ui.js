const fs = require("fs");
let ui = fs.readFileSync("src/i18n/ui.ts", "utf-8");

ui = ui.replace(
	/"sidebar\.phone": import\.meta\.env\.CONTACT_PHONE \|\| "0748198534"/g,
	`"sidebar.phone": (typeof import.meta !== "undefined" && import.meta.env && import.meta.env.CONTACT_PHONE) || "0748198534"`,
);

fs.writeFileSync("src/i18n/ui.ts", ui);
