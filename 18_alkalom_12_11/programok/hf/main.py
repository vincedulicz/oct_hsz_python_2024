from o_18_alkalom_12_11.hf.Autopark.Autopark import Autopark
from o_18_alkalom_12_11.hf.Jarmuvek.Teherauto import Teherauto
from o_18_alkalom_12_11.hf.Jarmuvek.Szemelygepkocsi import Szemelygepkocsi
from o_18_alkalom_12_11.hf.Dataprocess.Dataprocess import DataProcess as dp

if __name__ == "__main__":
    autopark = Autopark()

    fajlnev = "autopark.json"
    autopark.betoltes_fajlbol(fajlnev)

    auto1 = Szemelygepkocsi("sedan", "toyota", 2020, "v6", 4, 700)
    auto2 = Teherauto("kamion", "volvo", 2018, "v120", 12000, 8)

    autopark.jarmu_hozzadas(auto1)
    autopark.jarmu_hozzadas(auto2)

    autopark.mentes_fajlba(fajlnev)

    szurt_jarmuvek = dp.szures_evjarat_alapjan(autopark.jarmuvek, 2019)
    for jarmu in szurt_jarmuvek:
        print(jarmu.jarmu_adatok())

    if dp.van_e_megfelelo_jarmu(autopark.jarmuvek, 2020):
        print("van 21-es vagy újabb autó")
    else:
        print("nincsen 21-es vagy újabb az autóparkban")