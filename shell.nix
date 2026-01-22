{ pkgs ? import <nixpkgs> { } }:
pkgs.mkShell {
  NIX_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath (with pkgs; [
    mesa
    libGL
    libglvnd
    xorg.libX11
    xorg.libXrandr
    xorg.libXcursor
    xorg.libXi
    xorg.libXtst
    xorg.libXrender
    xorg.libXfixes
    xorg.libXext
    xorg.libSM
    xorg.libICE
    xorg.libXau
    xorg.libXdmcp
    freetype
  ]);

  NIX_LD = pkgs.lib.fileContents "${pkgs.stdenv.cc}/nix-support/dynamic-linker";

  shellHook = ''
    export LD_LIBRARY_PATH=$NIX_LD_LIBRARY_PATH
  '';
}

