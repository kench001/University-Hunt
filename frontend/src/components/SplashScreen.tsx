import { motion } from 'framer-motion'
import { GraduationCap } from 'lucide-react'

export default function SplashScreen() {
  return (
    <motion.div
      initial={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1] }}
      className="fixed inset-0 z-[100] flex flex-col items-center justify-center bg-midnight overflow-hidden"
    >
      {/* Decorative Gradients */}
      <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-sunset-orange/10 blur-[120px] rounded-full" />
      <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-sunset-orange/5 blur-[120px] rounded-full" />

      <div className="relative flex flex-col items-center">
        <motion.div
          initial={{ scale: 0.8, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          transition={{ 
            duration: 1, 
            ease: [0.22, 1, 0.36, 1],
            delay: 0.2
          }}
          className="w-20 h-20 bg-sunset-orange rounded-2xl flex items-center justify-center text-white mb-8 shadow-2xl shadow-sunset-orange/20"
        >
          <GraduationCap size={40} />
        </motion.div>

        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ 
            duration: 0.8, 
            ease: [0.22, 1, 0.36, 1],
            delay: 0.4
          }}
          className="text-center"
        >
          <h1 className="text-4xl md:text-5xl font-serif text-white font-bold tracking-tight mb-2">
            University Hunt
          </h1>
          <p className="text-sunset-orange/60 font-sans text-xs font-bold uppercase tracking-[0.3em]">
            Mapping Your Future
          </p>
        </motion.div>

        {/* Loading Bar */}
        <div className="mt-12 w-48 h-[2px] bg-white/5 rounded-full overflow-hidden">
          <motion.div
            initial={{ x: "-100%" }}
            animate={{ x: "0%" }}
            transition={{ 
              duration: 2, 
              ease: "easeInOut",
              repeat: 0
            }}
            className="h-full w-full bg-sunset-orange"
          />
        </div>
      </div>

      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1.5 }}
        className="absolute bottom-12 text-white/20 text-[10px] font-bold uppercase tracking-[0.2em]"
      >
        Metro Manila Education Guide
      </motion.div>
    </motion.div>
  )
}
