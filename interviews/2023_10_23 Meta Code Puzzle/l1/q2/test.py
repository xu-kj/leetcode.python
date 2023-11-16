from v1 import getArtisticPhotographCount

if __name__ == "__main__":
    print(getArtisticPhotographCount(
        N=5,
        C="APABA",
        X=1,
        Y=2))
    print(getArtisticPhotographCount(
        N=5,
        C="APABA",
        X=2,
        Y=3))
    print(getArtisticPhotographCount(
        N=8,
        C=".PBAAP.B",
        X=1,
        Y=3))
