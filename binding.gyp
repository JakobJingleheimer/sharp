{
  'targets': [{
    'target_name': 'sharp',
    'sources': ['src/sharp.cc'],
    'libraries': [
      '<!@(PKG_CONFIG_PATH="/usr/local/lib/pkgconfig" pkg-config --libs vips)',
      '<!@(PKG_CONFIG_PATH="/usr/lib/pkgconfig" pkg-config --libs vips)'
    ],
    'include_dirs': [
      '/usr/include/glib-2.0',
      '/usr/lib/glib-2.0/include',
      '/usr/lib/x86_64-linux-gnu/glib-2.0/include'
    ],
    'cflags': ['-fexceptions'],
    'cflags_cc': ['-fexceptions']
  }]
}