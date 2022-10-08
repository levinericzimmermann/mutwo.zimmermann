with import <nixpkgs> {};
with pkgs.python3Packages;

let

  mutwo-core-archive = builtins.fetchTarball "https://github.com/mutwo-org/mutwo.core/archive/97aea97f996973955889630c437ceaea405ea0a7.tar.gz";
  mutwo-core = import (mutwo-core-archive + "/default.nix");

  mutwo-common-archive = builtins.fetchTarball "https://github.com/mutwo-org/mutwo.common/archive/9a0f12a72b5b6224b8a55227273a4fe6870c6300.tar.gz";
  mutwo-common = import (mutwo-common-archive + "/default.nix");

  mutwo-music-archive = builtins.fetchTarball "https://github.com/mutwo-org/mutwo.music/archive/4e4369c1c9bb599f47ec65eb86f87e9179e17d97.tar.gz";
  mutwo-music = import (mutwo-music-archive + "/default.nix");

in

  buildPythonPackage rec {
    name = "mutwo.zimmermann";
    src = fetchFromGitHub {
      owner = "mutwo-org";
      repo = name;
      rev = "bd04b339b6cff0d0b679ed61f1d506869ab8b088";
      sha256 = "sha256-ml3kIVHLiWo6GbipEFFOx/s+bMDVNqibgN1wZgpRECI=";
    };
    propagatedBuildInputs = [ 
      python39Packages.sympy
      mutwo-core
      mutwo-common
      mutwo-music
    ];
    doCheck = true;
  }
