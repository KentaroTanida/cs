# Install wkhtmltopdf on macOS

```
$ brew update

$ brew search wkhtmltopdf
==> Casks
homebrew/cask/wkhtmltopdf

$ brew cask install wkhtmltopdf
==> Tapping homebrew/cask
Cloning into '/usr/local/Homebrew/Library/Taps/homebrew/homebrew-cask'...
remote: Enumerating objects: 4090, done.
remote: Counting objects: 100% (4090/4090), done.
remote: Compressing objects: 100% (4073/4073), done.
remote: Total 4090 (delta 23), reused 676 (delta 14), pack-reused 0
Receiving objects: 100% (4090/4090), 1.31 MiB | 9.71 MiB/s, done.
Resolving deltas: 100% (23/23), done.
Tapped 1 command and 3988 casks (4,096 files, 4.2MB).
==> Caveats
Cask wkhtmltopdf installs files under /usr/local. The presence of such
files can cause warnings when running "brew doctor", which is considered
to be a bug in Homebrew Cask.

==> Satisfying dependencies
==> Downloading https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox-0.12.5-1.macos-cocoa.pkg
==> Downloading from https://github-production-release-asset-2e65be.s3.amazonaws.com/271714/501d30f4-
######################################################################## 100.0%
==> Verifying SHA-256 checksum for Cask 'wkhtmltopdf'.
==> Installing Cask wkhtmltopdf
==> Creating Caskroom at /usr/local/Caskroom
==> We'll set permissions properly so we won't need sudo in the future.
Password:
==> Running installer for wkhtmltopdf; your password may be necessary.
==> Package installers may write to any location; options such as --appdir are ignored.
installer: Package name is wkhtmltox-0.12.5-1.macos-cocoa
installer: Installing at base path /
installer: The install was successful.
🍺  wkhtmltopdf was successfully installed!

$ which wkhtmltopdf
/usr/local/bin/wkhtmltopdf

$ wkhtmltopdf -V
wkhtmltopdf 0.12.5 (with patched qt)
```


## ipynb to html

```
ls *.ipynb | xargs -I{} jupyter nbconvert --to html {}
```


## html to pdf

```
ls *.html | cut -f1 -d'.' | xargs -I{} wkhtmltopdf {}.html {}.pdf
```





