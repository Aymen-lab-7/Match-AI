// lib/data.ts

export interface DupeProduct {
  category: 'skin' | 'fashion';
  original: string;
  originalPrice: number;
  originalImg: string;
  dupe: string;
  dupePrice: number;
  dupeImg: string;
  match: number;
  details: string[];
}

export const DUPES_DATA: DupeProduct[] = [
  { 
    category: "skin", 
    original: "La Mer Moisturizing Cream", 
    originalPrice: 190, 
    originalImg: "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400",
    dupe: "CeraVe Moisturizing Cream", 
    dupePrice: 16, 
    dupeImg: "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400",
    match: 94, 
    details: ["Sea Kelp vs Ceramides", "Rich Texture", "Fragrance Free"]
  },
  { 
    category: "skin", 
    original: "SkinCeuticals C E Ferulic", 
    originalPrice: 182, 
    originalImg: "https://images.unsplash.com/photo-1621233341330-34820ddad0d0?w=400",
    dupe: "Timeless Vitamin C Serum", 
    dupePrice: 26, 
    dupeImg: "https://images.unsplash.com/photo-1617897903246-719242758050?w=400",
    match: 91, 
    details: ["L-Ascorbic Acid", "Ferulic Acid", "Anti-Aging Focus"]
  },
  { 
    category: "fashion", 
    original: "Hermès Birkin 25", 
    originalPrice: 12000, 
    originalImg: "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=400",
    dupe: "Lily & Bean Hattie Bag", 
    dupePrice: 150, 
    dupeImg: "https://images.unsplash.com/photo-1591561954557-26941169b49e?w=400",
    match: 85, 
    details: ["Real Leather", "Gold Hardware", "Similar Silhouette"]
  },
  { 
    category: "fashion", 
    original: "Chanel Tweed Jacket", 
    originalPrice: 6500, 
    originalImg: "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=400",
    dupe: "Zara Textured Jacket", 
    dupePrice: 89, 
    dupeImg: "https://images.unsplash.com/photo-1539533113208-f6df8cc8b543?w=400",
    match: 82, 
    details: ["Tweed Pattern", "Decorative Buttons", "Cropped Fit"]
  }
];