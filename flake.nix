{
  description = "A Nix-flake-based Python development environment";
  # External flakes dependencies
  inputs.nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/0.1.*.tar.gz";

  # define what your flake provides: devShells, packages, apps, etc.
  outputs = { self, nixpkgs }:
    let
      # List of supported systems
      supportedSystems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      # Helper function to generate devShells for all supported systems
      forEachSupportedSystem = f: nixpkgs.lib.genAttrs supportedSystems (system: f {
        # Import the nixpkgs package set for the current system
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      devShells = forEachSupportedSystem ({ pkgs }: {
        # Default devShell configuration
        default = pkgs.mkShell {
          # Directory for virtual environment
          venvDir = ".venv";
          # Define the packages to be installed in the devShell 
          packages = with pkgs; [
            # Python 3.11
            python311
          ] ++ (with pkgs.python311Packages; [
              pip
              venvShellHook
            ]);
        };
      });
    };
}
