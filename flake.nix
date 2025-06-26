{
  inputs = {
    utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, utils }: utils.lib.eachDefaultSystem (system:
    let
      pkgs = nixpkgs.legacyPackages.${system};
      pythonEnv = pkgs.python313.withPackages ( ps: with ps; [] );
    in
      {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
            uv
            pythonEnv
            pkgs.zlib
            pkgs.stdenv.cc.cc.lib
            wget2
            # libsForQt5.wrapQtAppsHook
            # (python313packages.matplotlib.override {
            #   enableQt = true;
            # })


          ];

          LD_LIBRARY_PATH = "${pkgs.lib.makeLibraryPath [
            pkgs.gcc-unwrapped.lib
            pkgs.zlib
          ]}:$LD_LIBRARY_PATH";
          

          UV_PYTHON="${pythonEnv}/bin/python";
          UV_PYTHON_PREFERENCE = "only-system";
          # shellHook = ''
          # '' ;
        };
      }
  );

}
