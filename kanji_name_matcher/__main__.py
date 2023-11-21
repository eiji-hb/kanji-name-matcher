from kanji_matcher.main import main

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('Interrupted.')
    sys.exit(1)
