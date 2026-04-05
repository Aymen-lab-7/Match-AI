'use client';
import { useState, ChangeEvent, useEffect } from 'react';
import { supabase } from '@/lib/supabase';

// 1. تعريف واجهة ml5 لإصلاح أخطاء TypeScript
declare global {
  interface Window {
    ml5: any;
  }
}

export default function Home() {
  const [tab, setTab] = useState<'skin' | 'fashion'>('skin');
  const [searchQuery, setSearchQuery] = useState("");
  const [products, setProducts] = useState<any[]>([]);
  const [analyzing, setAnalyzing] = useState(false);

  // 2. أسرع طريقة للأفلييت: استخدام محول تلقائي (Auto-Redirect)
  // بدلاً من توليد روابط يدوية، نرسل المستخدم لمحول ذكي
  const getFastAffiliateLink = (originalUrl: string) => {
    // إذا كنت تستخدم Skimlinks أو Impact Deep Linking
    // هذا الرابط يحول أي منتج لرابط ربحي فوراً
    const redirectTool = "https://go.skimlinks.com/?id=YOUR_ID&url="; 
    return `${redirectTool}${encodeURIComponent(originalUrl)}`;
  };

  const searchWebForMatches = async (productName: string) => {
    if (!productName || productName === "Scanning...") return;
    setProducts([]); 
    setAnalyzing(true);

    try {
      const categoryHint = tab === 'skin' ? 'skincare dupe' : 'fashion affordable match';
      const response = await fetch(`/api/search?q=${encodeURIComponent(productName + " " + categoryHint)}`);
      const data = await response.json();

      if (data.shopping_results) {
        const formatted = data.shopping_results.slice(0, 8).map((item: any) => ({
          id: item.product_id || Math.random().toString(),
          name: item.title,
          price: item.price,
          img: item.thumbnail,
          link: item.link,
          source: item.source
        }));
        setProducts(formatted);
      }
    } catch (e) {
      console.error(e);
    } finally {
      setAnalyzing(false);
    }
  };

  const saveToSupabase = async (product: any) => {
    const { error } = await supabase.from('saved_dupes').insert([{ 
      name: product.name, price: product.price, image: product.img, link: product.link, category: tab 
    }]);
    if (!error) alert("✨ Added to collection!");
  };

  const handleImageUpload = (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setAnalyzing(true);
    setSearchQuery("Scanning...");
    const img = document.createElement('img');
    img.src = URL.createObjectURL(file);
    img.onload = async () => {
      if (window.ml5) {
        const classifier = await window.ml5.imageClassifier('MobileNet');
        classifier.classify(img, (err: any, results: any) => {
          if (results?.[0]) {
            const label = results[0].label.split(',')[0];
            setSearchQuery(label);
            searchWebForMatches(label);
          }
        });
      }
    };
  };

  return (
    <main className="min-h-screen bg-black text-white p-4 md:p-8 selection:bg-[#C9A96E]/30">
      <div className="max-w-5xl mx-auto">
        
        {/* Header */}
        <header className="text-center mb-12">
          <h1 className="text-3xl md:text-5xl text-[#C9A96E] font-serif tracking-[0.2em] uppercase mb-2">MATCH AI</h1>
          <p className="text-[8px] tracking-[0.4em] text-zinc-500 uppercase italic">Automated Affiliate Engine v1.0</p>
        </header>

        {/* Search & Camera */}
        <div className="relative mb-16">
          <input 
            type="text" value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && searchWebForMatches(searchQuery)}
            placeholder="SCAN OR TYPE PRODUCT..."
            className="w-full bg-transparent border-b border-zinc-800 py-6 text-xl md:text-2xl font-serif focus:outline-none focus:border-[#C9A96E] uppercase transition-all"
          />
          <label className="absolute right-0 top-6 cursor-pointer">
            <input type="file" accept="image/*" className="hidden" onChange={handleImageUpload} />
            <span className={`text-2xl ${analyzing ? 'animate-pulse text-[#C9A96E]' : 'opacity-40'}`}>📷</span>
          </label>
        </div>

        {/* Grid Results */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {products.map((item) => (
            <div key={item.id} className="p-4 border border-zinc-900 bg-zinc-950/40 rounded-xl flex gap-4 items-center group relative">
              <button onClick={() => saveToSupabase(item)} className="absolute top-4 right-4 text-[#C9A96E] opacity-0 group-hover:opacity-100 transition-all">❤️</button>
              <div className="w-24 h-24 bg-white rounded-lg p-1 flex-shrink-0">
                <img src={item.img} className="w-full h-full object-contain" alt="" />
              </div>
              <div className="flex-1">
                <span className="text-[7px] text-[#C9A96E] font-bold uppercase tracking-widest">{item.source}</span>
                <h3 className="text-[11px] text-zinc-100 line-clamp-2 mb-1">{item.name}</h3>
                <p className="text-xl font-light mb-2">{item.price}</p>
                <a 
                  href={getFastAffiliateLink(item.link)} 
                  target="_blank" 
                  className="inline-block text-[8px] tracking-widest uppercase text-[#C9A96E] border border-[#C9A96E]/30 px-4 py-1.5 rounded-full hover:bg-[#C9A96E] hover:text-black transition-all"
                >
                  Buy Now & Support Us
                </a>
              </div>
            </div>
          ))}
        </div>

        {/* Affiliate Disclosure - ضروري جداً لعدم الحظر */}
        <footer className="mt-20 pt-10 border-t border-zinc-900 pb-10">
          <div className="bg-zinc-950/50 p-6 rounded-xl border border-zinc-900/30">
            <p className="text-zinc-500 text-[8px] uppercase tracking-[0.2em] leading-relaxed">
              Match AI is a diagnostic tool that helps you find product alternatives. We may earn a commission from qualifying purchases made through our links to various retailers. This does not affect the price you pay.
            </p>
          </div>
        </footer>

        {analyzing && <div className="text-center py-10 text-[#C9A96E] animate-pulse text-[10px] tracking-[0.5em]">ANALYZING...</div>}
      </div>
    </main>
  );
}