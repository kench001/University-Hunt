import { useState, useEffect, useRef } from 'react'
import universityDataRaw from './data/metro_manila_universities.json'
const universityData = universityDataRaw as {
  cities: {
    name: string
    universities: University[]
  }[]
}

import { Search, GitCompare as CompareIcon, MapPin, GraduationCap, DollarSign, BookOpen, ChevronLeft, Globe, Award, Heart, List, Map as MapIcon, ArrowUpRight, X } from 'lucide-react'
import { motion, AnimatePresence } from 'framer-motion'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'
import L from 'leaflet'
import SplashScreen from './components/SplashScreen'

// Fix for default Leaflet marker icons in React
import markerIcon from 'leaflet/dist/images/marker-icon.png';
import markerShadow from 'leaflet/dist/images/marker-shadow.png';
let DefaultIcon = L.icon({
    iconUrl: markerIcon,
    shadowUrl: markerShadow,
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});
L.Marker.prototype.options.icon = DefaultIcon;

// Types
type University = {
  name: string
  type: string
  website: string
  info: string
  ph_ranking: string
  qs_asia_rank_2026: string | number
  acceptance_rate: string
  total_estimated_students: string
  programs: string[]
  tuition: any 
  city?: string
  tuition_min?: number
  tuition_max?: number
  categories?: string[]
  lat?: number
  lng?: number
}

export default function App() {
  // --- STATE ---
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedCity, setSelectedCity] = useState<string>('All')
  const [selectedCategory, setSelectedCategory] = useState<string>('All')
  const [maxBudget, setMaxBudget] = useState<number>(500000)
  const [viewMode, setViewMode] = useState<'list' | 'map'>('list')
  
  const [compareList, setCompareList] = useState<University[]>([])
  const [favorites, setFavorites] = useState<string[]>([]) 
  const [isComparing, setIsComparing] = useState(false)
  const [isDrawerOpen, setIsDrawerOpen] = useState(false)
  const [selectedUni, setSelectedUni] = useState<University | null>(null)
  const [isLoading, setIsLoading] = useState(true)

  const searchRef = useRef<HTMLDivElement>(null)

  // --- EFFECTS ---
  useEffect(() => {
    const timer = setTimeout(() => setIsLoading(false), 2500)
    const savedFavs = localStorage.getItem('uni-hunt-favs')
    if (savedFavs) setFavorites(JSON.parse(savedFavs))
    return () => clearTimeout(timer)
  }, [])

  useEffect(() => {
    localStorage.setItem('uni-hunt-favs', JSON.stringify(favorites))
  }, [favorites])

  // --- LOGIC ---
  const scrollToSearch = () => {
    searchRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  const allUniversities = universityData.cities.flatMap(city => 
    city.universities.map(u => ({ ...u, city: city.name }))
  )

  const categories = ['All', 'Medical', 'Engineering & Tech', 'Business & Law', 'Arts & Humanities', 'Education']
  const cities = ['All', ...universityData.cities.map(c => c.name)]

  const filteredUniversities = allUniversities.filter(u => {
    const matchesSearch = u.name.toLowerCase().includes(searchTerm.toLowerCase()) || 
                         u.programs?.some(p => p.toLowerCase().includes(searchTerm.toLowerCase()))
    const matchesCity = selectedCity === 'All' || u.city === selectedCity
    const matchesCategory = selectedCategory === 'All' || u.categories?.includes(selectedCategory)
    const matchesBudget = (u.tuition_min ?? 0) <= maxBudget
    return matchesSearch && matchesCity && matchesCategory && matchesBudget
  })

  const toggleCompare = (e: React.MouseEvent, uni: University) => {
    e.stopPropagation()
    if (compareList.some(u => u.name === uni.name)) {
      setCompareList(compareList.filter(u => u.name !== uni.name))
    } else if (compareList.length < 2) {
      setCompareList([...compareList, uni])
    }
  }

  const toggleFavorite = (e: React.MouseEvent, uniName: string) => {
    e.stopPropagation()
    setFavorites(prev => 
      prev.includes(uniName) ? prev.filter(name => name !== uniName) : [...prev, uniName]
    )
  }

  return (
    <div className="min-h-screen font-sans bg-sky-mist">
      <AnimatePresence mode="wait">
        {isLoading ? (
          <SplashScreen key="splash" />
        ) : (
          <motion.div key="content" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.8 }}>
            
            {/* NAVIGATION */}
            <nav className="fixed top-0 left-0 w-full z-50 bg-white/70 backdrop-blur-md border-b border-black/5 px-8 h-16 flex items-center">
              <div className="max-w-7xl mx-auto w-full flex justify-between items-center">
                <div className="flex items-center gap-2 cursor-pointer" onClick={() => setSelectedUni(null)}>
                  <div className="w-8 h-8 bg-midnight rounded-lg flex items-center justify-center text-white">
                    <GraduationCap size={20} />
                  </div>
                  <span className="text-xl font-display font-bold tracking-tight">University Hunt</span>
                </div>
                
                <div className="flex items-center gap-4">
                  <button onClick={() => setIsDrawerOpen(true)} className="relative p-2 text-midnight/60 hover:text-sunset-orange transition-colors">
                    <Heart size={24} fill={favorites.length > 0 ? "#FF7A2E" : "none"} />
                    {favorites.length > 0 && (
                      <span className="absolute top-0 right-0 bg-sunset-orange text-white text-[10px] font-bold w-4 h-4 rounded-full flex items-center justify-center">
                        {favorites.length}
                      </span>
                    )}
                  </button>
                  <button onClick={scrollToSearch} className="bg-midnight text-white px-6 py-2 rounded-full text-sm font-bold flex items-center gap-2 group hover:bg-midnight/90 transition-all">
                    Start hunt
                    <div className="bg-sunset-orange w-5 h-5 rounded flex items-center justify-center transition-transform group-hover:translate-x-1 group-hover:-translate-y-1">
                      <ArrowUpRight size={14} className="text-white" />
                    </div>
                  </button>
                </div>
              </div>
            </nav>

            {/* FAVORITES DRAWER */}
            <AnimatePresence>
              {isDrawerOpen && (
                <>
                  <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} onClick={() => setIsDrawerOpen(false)} className="fixed inset-0 bg-midnight/20 backdrop-blur-sm z-[60]" />
                  <motion.div initial={{ x: '100%' }} animate={{ x: 0 }} exit={{ x: '100%' }} transition={{ type: 'spring', damping: 25, stiffness: 200 }} className="fixed right-0 top-0 h-full w-full max-w-md bg-white z-[70] shadow-2xl p-8 overflow-y-auto">
                    <div className="flex justify-between items-center mb-12">
                      <h2 className="text-3xl font-display font-bold">My Shortlist</h2>
                      <button onClick={() => setIsDrawerOpen(false)} className="p-2 hover:bg-sky-mist rounded-full transition-colors"><X size={24} /></button>
                    </div>
                    <div className="space-y-6">
                      {favorites.length > 0 ? (
                        allUniversities.filter(u => favorites.includes(u.name)).map(uni => (
                          <div key={uni.name} className="p-4 border border-black/5 rounded-2xl flex justify-between items-center group hover:bg-sky-mist transition-colors">
                            <div className="cursor-pointer flex-grow" onClick={() => { setSelectedUni(uni); setIsDrawerOpen(false); }}>
                              <p className="font-bold text-midnight">{uni.name}</p>
                              <p className="text-xs text-muted-steel">{uni.city}</p>
                            </div>
                            <button onClick={(e) => toggleFavorite(e, uni.name)} className="text-sunset-orange p-2"><Heart size={20} fill="#FF7A2E" /></button>
                          </div>
                        ))
                      ) : (
                        <div className="text-center py-20 text-muted-steel"><Heart size={48} className="mx-auto mb-4 opacity-20" /><p>Your shortlist is empty.</p></div>
                      )}
                    </div>
                  </motion.div>
                </>
              )}
            </AnimatePresence>

            <AnimatePresence mode="wait">
              {!selectedUni ? (
                <motion.div key="listing" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="pt-16">
                  <header className="sky-bg pt-24 pb-32 px-8 text-center relative overflow-hidden">
                    <div className="max-w-4xl mx-auto relative z-10">
                      <motion.div initial={{ y: 30, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 1 }}>
                        <div className="inline-flex items-center gap-2 bg-white/50 backdrop-blur-sm border border-black/5 px-4 py-1.5 rounded-full mb-8 shadow-sm">
                          <div className="w-2 h-2 rounded-full bg-sunset-orange animate-pulse" />
                          <span className="text-[10px] font-bold uppercase tracking-[0.2em] text-midnight/50">2026 Admissions Now Open</span>
                        </div>
                        <h1 className="text-6xl md:text-8xl font-display mb-8 leading-[1.1] tracking-tight">One portal for every <br /><span className="text-sunset-orange">student & university</span></h1>
                        <p className="text-lg md:text-xl text-muted-steel max-w-2xl mx-auto mb-12 leading-relaxed">Search, compare, and plan your academic future with a modern, structured guide to Metro Manila's top institutions.</p>
                        <div className="flex flex-wrap justify-center gap-4 mb-20">
                          <button onClick={scrollToSearch} className="bg-midnight text-white px-8 py-4 rounded-full font-bold flex items-center gap-3 group shadow-xl hover:shadow-sunset-orange/20 transition-all">
                            Search Universities
                            <div className="bg-sunset-orange w-6 h-6 rounded flex items-center justify-center transition-transform group-hover:translate-x-1 group-hover:-translate-y-1"><ArrowUpRight size={16} className="text-white" /></div>
                          </button>
                        </div>
                      </motion.div>
                    </div>
                  </header>

                  {/* SEARCH & FILTERS BAR */}
                  <div ref={searchRef} className="sticky top-16 z-40 px-8 py-3 bg-sky-mist/80 backdrop-blur-md border-b border-black/5">
                    <div className="max-w-5xl mx-auto">
                      <div className="flex flex-col md:flex-row items-center bg-white rounded-3xl md:rounded-full shadow-premium border border-black/5 p-1.5 transition-all gap-2 md:gap-0">
                        <div className="relative flex-grow w-full">
                          <Search className="absolute left-6 top-1/2 -translate-y-1/2 text-midnight/30" size={20} />
                          <input type="text" placeholder="Search schools or programs..." className="w-full pl-14 py-3 text-lg bg-transparent border-none focus:outline-none placeholder:text-midnight/30" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)} />
                        </div>
                        <div className="soft-divider" />
                        <div className="flex items-center gap-2 w-full md:w-auto px-4">
                          <select className="bg-transparent py-3 text-sm font-medium focus:outline-none cursor-pointer hover:text-sunset-orange transition-colors appearance-none" value={selectedCity} onChange={(e) => setSelectedCity(e.target.value)}>{cities.map(city => <option key={city} value={city}>{city}</option>)}</select>
                          <div className="soft-divider" />
                          <select className="bg-transparent py-3 text-sm font-medium focus:outline-none cursor-pointer hover:text-sunset-orange transition-colors appearance-none" value={selectedCategory} onChange={(e) => setSelectedCategory(e.target.value)}>{categories.map(cat => <option key={cat} value={cat}>{cat}</option>)}</select>
                        </div>
                        <button onClick={() => setIsComparing(!isComparing)} className={`w-full md:w-auto soft-button !px-8 !py-3 whitespace-nowrap ${compareList.length === 2 ? 'bg-sunset-orange text-white' : 'bg-midnight text-white'}`}><CompareIcon size={16} /> {isComparing ? 'Close' : `Compare (${compareList.length}/2)`}</button>
                      </div>
                      <div className="mt-4 px-6 flex items-center gap-4">
                        <span className="text-[10px] font-bold text-midnight/40 uppercase tracking-widest flex items-center gap-1"><DollarSign size={12} /> Max Budget: ₱{maxBudget.toLocaleString()}</span>
                        <input type="range" min="0" max="500000" step="5000" value={maxBudget} onChange={(e) => setMaxBudget(parseInt(e.target.value))} className="flex-grow h-1 bg-black/10 rounded-lg appearance-none cursor-pointer accent-sunset-orange" />
                      </div>
                    </div>
                  </div>

                  <main className="max-w-7xl mx-auto px-8 py-16">
                    <div className="flex justify-end mb-8 gap-2">
                      <button onClick={() => setViewMode('list')} className={`p-3 rounded-xl transition-all ${viewMode === 'list' ? 'bg-midnight text-white' : 'bg-white text-midnight border border-black/5'}`}><List size={20} /></button>
                      <button onClick={() => setViewMode('map')} className={`p-3 rounded-xl transition-all ${viewMode === 'map' ? 'bg-midnight text-white' : 'bg-white text-midnight border border-black/5'}`}><MapIcon size={20} /></button>
                    </div>

                    <AnimatePresence mode="wait">
                      {isComparing && compareList.length === 2 ? (
                        <motion.div key="comparison" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }} className="overflow-x-auto">
                          <div className="min-w-[600px] bg-white rounded-3xl border border-black/5 shadow-premium overflow-hidden">
                            <table className="w-full text-left border-collapse">
                              <thead>
                                <tr className="bg-midnight text-white">
                                  <th className="p-6 text-sm font-bold uppercase tracking-widest opacity-60">Metric</th>
                                  {compareList.map(u => <th key={u.name} className="p-6 text-xl font-display">{u.name}</th>)}
                                </tr>
                              </thead>
                              <tbody className="divide-y divide-black/5">
                                {[
                                  { label: 'Type', key: 'type' },
                                  { label: 'Location', key: 'city' },
                                  { label: 'PH Rank', key: 'ph_ranking' },
                                  { label: 'Asia Rank', key: 'qs_asia_rank_2026' },
                                  { label: 'Acceptance', key: 'acceptance_rate' },
                                  { label: 'Min Tuition', key: 'tuition_min', isPrice: true },
                                ].map(row => (
                                  <tr key={row.label} className="hover:bg-sky-mist transition-colors">
                                    <td className="p-6 font-bold text-xs uppercase tracking-widest text-midnight/40">{row.label}</td>
                                    {compareList.map(u => (
                                      <td key={u.name} className="p-6 font-medium">
                                        {row.isPrice ? `₱${(u[row.key as keyof University] as number)?.toLocaleString()}` : (u[row.key as keyof University] as string)}
                                      </td>
                                    ))}
                                  </tr>
                                ))}
                              </tbody>
                            </table>
                          </div>
                        </motion.div>
                      ) : viewMode === 'map' ? (
                        <motion.div key="map" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="h-[600px] rounded-3xl overflow-hidden border border-black/5 shadow-premium">
                          <MapContainer center={[14.5995, 120.9842]} zoom={11} style={{ height: '100%', width: '100%' }}>
                            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
                            {filteredUniversities.filter(u => u.lat && u.lng).map(uni => (
                              <Marker key={uni.name} position={[uni.lat!, uni.lng!]} eventHandlers={{ click: () => setSelectedUni(uni) }}>
                                <Popup>
                                  <div className="p-2">
                                    <p className="font-bold">{uni.name}</p>
                                    <p className="text-xs text-muted-steel">{uni.city}</p>
                                    <button onClick={() => setSelectedUni(uni)} className="text-sunset-orange text-[10px] font-bold uppercase mt-2 underline">View Details</button>
                                </div>
                                </Popup>
                              </Marker>
                            ))}
                          </MapContainer>
                        </motion.div>
                      ) : (
                        <motion.div key="list" initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                          {filteredUniversities.length > 0 ? (
                            filteredUniversities.map((uni, idx) => (
                              <motion.div key={uni.name} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: idx * 0.05 }}>
                                <UniversityCard uni={uni} onCompare={toggleCompare} compareList={compareList} onClick={() => setSelectedUni(uni)} favorites={favorites} onFavorite={toggleFavorite} />
                              </motion.div>
                            ))
                          ) : (
                            <div className="col-span-full py-32 text-center">
                              <GraduationCap size={64} className="mx-auto mb-6 text-midnight/5" />
                              <h2 className="text-4xl mb-4">No schools matched your hunt.</h2>
                              <p className="text-muted-steel font-bold uppercase tracking-widest text-sm">Try adjusting your budget or category</p>
                            </div>
                          )}
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </main>
                </motion.div>
              ) : (
                <motion.div key="detail" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="min-h-screen bg-white pt-20">
                  <div className="max-w-7xl mx-auto px-8 py-12">
                    <button onClick={() => setSelectedUni(null)} className="flex items-center gap-2 text-muted-steel hover:text-midnight mb-12 transition-colors font-bold uppercase text-xs tracking-widest"><ChevronLeft size={16} /> Back to Search</button>
                    <div className="flex flex-col lg:flex-row gap-16 items-start">
                      <div className="flex-grow">
                        <div className="flex justify-between items-start">
                          <div className="inline-flex gap-2 items-center mb-6">
                            <span className="soft-tag bg-sunset-orange/10 text-sunset-orange">{selectedUni.type}</span>
                            <span className="soft-tag bg-midnight/5 text-midnight/40">{selectedUni.city}</span>
                          </div>
                          <button onClick={(e) => toggleFavorite(e, selectedUni.name)} className={`p-3 rounded-full border transition-all ${favorites.includes(selectedUni.name) ? 'bg-sunset-orange text-white border-sunset-orange' : 'bg-white text-midnight border-black/10 hover:border-sunset-orange'}`}><Heart size={20} fill={favorites.includes(selectedUni.name) ? "#fff" : "none"} /></button>
                        </div>
                        <h1 className="text-5xl md:text-7xl mb-8">{selectedUni.name}</h1>
                        <p className="text-xl text-muted-steel leading-relaxed mb-12 max-w-3xl">{selectedUni.info}</p>
                        
                        <section className="mb-12">
                           <h3 className="text-2xl font-bold mb-6 flex items-center gap-2"><DollarSign size={24} className="text-sunset-orange" /> Tuition Fees</h3>
                           <div className="grid grid-cols-1 gap-4">
                              {typeof selectedUni.tuition === 'object' ? (
                                Object.entries(selectedUni.tuition as Record<string, string>).map(([key, value]) => (
                                  <div key={key} className="p-6 bg-sky-mist rounded-2xl border border-black/5 flex justify-between items-center">
                                    <span className="font-bold uppercase text-[10px] text-midnight/40">{key.replace(/_/g, ' ')}</span>
                                    <span className="font-medium">{String(value)}</span>
                                  </div>
                                ))
                              ) : (
                                <div className="p-6 bg-sky-mist rounded-2xl border border-black/5 flex justify-between items-center">
                                  <span className="font-bold uppercase text-[10px] text-midnight/40">Estimated Tuition</span>
                                  <span className="font-medium">{String(selectedUni.tuition)}</span>
                                </div>
                              )}
                           </div>
                        </section>
                        <section>
                           <h3 className="text-2xl font-bold mb-6 flex items-center gap-2"><BookOpen size={24} className="text-sunset-orange" /> Featured Programs</h3>
                           <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                             {selectedUni.programs.map(p => (
                               <div key={p} className="p-4 bg-sky-mist rounded-xl border border-black/5 font-medium flex justify-between items-center group cursor-default hover:bg-white hover:shadow-premium transition-all">
                                 {p} <ArrowUpRight size={14} className="opacity-0 group-hover:opacity-30 transition-opacity" />
                               </div>
                             ))}
                           </div>
                        </section>
                      </div>
                      <div className="w-full lg:w-72">
                        <div className="bg-white rounded-[32px] p-8 border border-black/5 shadow-premium sticky top-32">
                          <div className="flex items-center gap-3 mb-8">
                            <div className="w-2 h-8 bg-gradient-to-b from-sunset-orange to-orange-400 rounded-full" />
                            <h4 className="text-xs font-bold uppercase tracking-[0.25em] text-midnight/40">Quick Summary</h4>
                          </div>
                          <div className="space-y-5">
                             {[
                                { icon: Award, label: 'Ranking', value: selectedUni.ph_ranking, color: 'sunset-orange', bgColor: 'bg-orange-50' },
                                { icon: Globe, label: 'Acceptance', value: selectedUni.acceptance_rate, color: 'midnight', bgColor: 'bg-slate-50' },
                                { icon: GraduationCap, label: 'Students', value: selectedUni.total_estimated_students, color: 'forest-green', bgColor: 'bg-emerald-50' },
                                { icon: MapPin, label: 'Campus', value: selectedUni.city, color: 'royal-purple', bgColor: 'bg-violet-50' }
                             ].map((item, i) => (
                               <div key={i} className="flex gap-4 items-center p-4 rounded-2xl hover:bg-gray-50 transition-all cursor-default">
                                 <div className={`w-12 h-12 ${item.bgColor} rounded-2xl flex items-center justify-center shrink-0`}><item.icon size={22} className="text-midnight/60" /></div>
                                 <div className="flex flex-col min-w-0">
                                   <span className="text-[10px] font-bold text-midnight/30 uppercase tracking-[0.15em]">{item.label}</span>
                                   <p className="text-sm font-bold text-midnight truncate">{item.value}</p>
                                 </div>
                               </div>
                             ))}
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>

            <footer className="bg-midnight text-white py-24 px-8 mt-20">
              <div className="max-w-7xl mx-auto text-center opacity-40 text-xs font-bold uppercase tracking-[0.2em]">
                © 2026 Metro Manila Education Guide. All rights reserved.
              </div>
            </footer>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}

function UniversityCard({ uni, onCompare, compareList, onClick, favorites, onFavorite }: { uni: University, onCompare: (e: React.MouseEvent, u: University) => void, compareList: University[], onClick: () => void, favorites: string[], onFavorite: (e: React.MouseEvent, name: string) => void }) {
  const isCompared = compareList.some(u => u.name === uni.name)
  const isFav = favorites.includes(uni.name)
  
  return (
    <div onClick={onClick} className="soft-card group cursor-pointer relative overflow-hidden flex flex-col h-full">
      <div className="flex justify-between items-start mb-6">
        <div className="flex gap-2 items-center">
          <span className={`soft-tag ${uni.type === 'Public' ? 'bg-sunset-orange/10 text-sunset-orange border-sunset-orange/10' : 'bg-midnight/5 text-midnight/40 border-midnight/5'}`}>{uni.type}</span>
          <span className="soft-tag bg-sky-mist text-muted-steel/60 italic">{uni.city}</span>
        </div>
        <div className="flex gap-2">
          <button onClick={(e) => onFavorite(e, uni.name)} className={`w-10 h-10 rounded-full border border-black/10 flex items-center justify-center transition-all ${isFav ? 'bg-sunset-orange text-white border-sunset-orange' : 'bg-white hover:text-sunset-orange'}`}><Heart size={16} fill={isFav ? "#fff" : "none"} /></button>
          <button onClick={(e) => onCompare(e, uni)} className={`w-10 h-10 rounded-full border border-black/10 flex items-center justify-center transition-all ${isCompared ? 'bg-sunset-orange text-white border-sunset-orange' : 'bg-white hover:text-sunset-orange'}`}><CompareIcon size={16} /></button>
        </div>
      </div>
      <h2 className="text-2xl mb-4 leading-tight font-display font-bold group-hover:text-sunset-orange transition-colors">{uni.name}</h2>
      <p className="text-sm text-muted-steel mb-8 line-clamp-2 leading-relaxed flex-grow">{uni.info}</p>
      <div className="flex flex-wrap gap-2 mb-8">
        {uni.programs?.slice(0, 3).map(p => (<span key={p} className="text-[10px] font-bold text-midnight/40 bg-sky-mist px-2.5 py-1 rounded-md uppercase tracking-widest">{p}</span>))}
        {uni.programs && uni.programs.length > 3 && <span className="text-[10px] font-bold text-sunset-orange">+{uni.programs.length - 3}</span>}
      </div>
      <div className="pt-6 border-t border-black/5 flex justify-between items-center mt-auto">
        <div className="flex flex-col">
          <span className="text-[9px] font-bold text-midnight/30 uppercase tracking-[0.2em]">Est. Min Tuition</span>
          <span className="font-display text-lg font-bold">{uni.tuition_min === 0 ? 'Free' : `₱${uni.tuition_min?.toLocaleString()}`}</span>
        </div>
        <div className="text-sunset-orange opacity-0 group-hover:opacity-100 transition-all flex items-center gap-1 font-bold text-[10px] uppercase tracking-widest">Details <ArrowUpRight size={12} /></div>
      </div>
    </div>
  )
}