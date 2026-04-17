import { defineCollection, z } from "astro:content";

const blogCollection = defineCollection({
	type: "content",
	schema: z.object({
		title: z.string(),
		date: z.date(),
		author: z.string(),
		image: z.string().optional(),
	}),
});

const servicesCollection = defineCollection({
	type: "content",
	schema: z.object({
		title: z.string(),
		date: z.date(),
		author: z.string(),
		image: z.string().optional(),
	}),
});

export const collections = {
	blog: blogCollection,
	services: servicesCollection,
};
