import { column, defineDb, defineTable } from "astro:db";

const ContactFormSubmissions = defineTable({
	columns: {
		id: column.number({ primaryKey: true }),
		name: column.text(),
		email: column.text(),
		message: column.text(),
		createdAt: column.date({ default: new Date() }),
	},
});

const QuizResults = defineTable({
	columns: {
		id: column.number({ primaryKey: true }),
		email: column.text(),
		score: column.number(),
		answers: column.json(),
		createdAt: column.date({ default: new Date() }),
	},
});

const UserInteractions = defineTable({
	columns: {
		id: column.number({ primaryKey: true }),
		userId: column.text({ optional: true }),
		action: column.text(),
		details: column.text({ optional: true }),
		createdAt: column.date({ default: new Date() }),
	},
});

export default defineDb({
	tables: {
		ContactFormSubmissions,
		QuizResults,
		UserInteractions,
	},
});
