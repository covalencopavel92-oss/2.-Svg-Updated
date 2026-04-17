import { defineAction } from "astro:actions";
import { ContactFormSubmissions, db, QuizResults } from "astro:db";
import { z } from "astro:schema";

export const server = {
	submitContactForm: defineAction({
		accept: "form",
		input: z.object({
			name: z.string().min(1, "Name is required"),
			email: z.string().email("Invalid email address"),
			subject: z.string().min(1, "Subject is required"),
			message: z.string().min(1, "Message is required"),
			honeypot: z.string().optional(),
		}),
		handler: async (input) => {
			// Honeypot check
			if (input.honeypot) {
				return { success: false, message: "Bot detected" };
			}

			try {
				await db.insert(ContactFormSubmissions).values({
					name: input.name,
					email: input.email,
					message: `Subject: ${input.subject}\n\n${input.message}`,
				});
				return { success: true, message: "Form submitted successfully!" };
			} catch (error) {
				console.error("Error saving contact form:", error);
				return { success: false, message: "Failed to submit form." };
			}
		},
	}),
	submitQuiz: defineAction({
		accept: "json",
		input: z.object({
			scoreType: z.enum(["seo", "web", "consult"]),
			answers: z.record(z.string(), z.string()).optional(),
		}),
		handler: async (input) => {
			try {
				// Here we'd save quiz data to the DB. For now, just simulating success.
				// We might want to pass an email to link it, but since the form doesn't ask for one yet,
				// we'll just insert a dummy email or omit if optional (schema requires email).
				// For now, let's just log and return success to update UI.
				await db.insert(QuizResults).values({
					email: "anonymous@quiz.com", // Replace with actual email if gathered later
					score:
						input.scoreType === "seo" ? 1 : input.scoreType === "web" ? 2 : 3,
					answers: input.answers || {},
				});
				return { success: true };
			} catch (error) {
				console.error("Error saving quiz result:", error);
				return { success: false, message: "Failed to save quiz results." };
			}
		},
	}),
};
