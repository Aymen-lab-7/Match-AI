// lib/supabase.ts
import { createClient } from '@supabase/supabase-js';

// الرابط مستخرج من Project ID الخاص بك
const supabaseUrl = 'https://gpioyslomolacqstkpcr.supabase.co'; 

// المفتاح الذي أرسلته أنت للتو
const supabaseKey = 'sb_publishable_2EN5ywLbb_ne3goXJ569uQ_CAfPlgP6'; 

export const supabase = createClient(supabaseUrl, supabaseKey);