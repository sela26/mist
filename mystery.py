import streamlit as st


def check_password():
    """Überprüft das eingegebene Passwort."""
    correct_password = "geheim123"  # Passwort für den Zugriff auf die Nachricht
    password_input = st.text_input("Passwort eingeben:", type="password")

    if st.button("Bestätigen"):
        if password_input == correct_password:
            st.balloons()
            st.success("Richtig! 😍 Hier ist deine geheime Nachricht: 🤩         "
                       "Hey Julian, wir müssen reden. Und zwar nicht über irgendeine Reise, sondern über die Reise – unsere vier Wochen "
                       "in Thailand! Und bevor du mit „Ich war da ja schon mal“ anfängst, lass mich kurz erklären, warum das hier eine ganz "
                       "andere Liga wird. Erstens: Drei befreundete Pärchen zusammen in einem der schönsten Länder der Welt – das wird nicht "
                       "nur eine Reise, das wird ein Highlight deines Lebens. Und hey, deine Freundin ist auch am Start! Stell dir mal vor: "
                       "Traumstrände, geile Stimmung und jeden Tag neue Abenteuer – mit den besten Leuten, die du dir wünschen kannst. Zweitens: "
                       "Dein Tauchschein! Du hast ihn, also nutz ihn! Thailand hat einige der schönsten Tauchspots der Welt – kristallklares Wasser, "
                       "bunte Korallenriffe und eine Unterwasserwelt, die du garantiert noch nicht komplett gesehen hast. Perfekte Gelegenheit, um richtig "
                       "abzutauchen (im besten Sinne). Drittens: Kampfsport! Wenn es irgendwo auf der Welt Sinn macht, deine Skills zu verbessern, dann in Thailand. "
                       "Die Wiege des Muay Thai! Stell dir vor, du trainierst mal in einem richtig guten Gym, lernst neue Techniken von echten Profis – und verbindest das "
                       "mit einem geilen Urlaub. Mehr kann man aus einem Trip kaum rausholen.Viertens: Ja, Reisen kostet Geld. Aber Thailand gibt dir für dein Geld einfach so "
                       "viel mehr als andere Reiseziele. Und seien wir ehrlich – vier Wochen legendäre Erinnerungen sind wohl die beste Investition, die man machen kann. "
                       "Fünftens: Uni-Kram. Ja, du hast noch was zu tun. Aber vier Wochen sind machbar, vor allem, wenn du vorher ein bisschen was wegschaffst. Und wenn’s hart auf hart kommt, gibt’s dort WLAN und ruhige Orte zum Arbeiten – "
                       "aber realistisch gesehen wirst du es nicht bereuen, mal für ein paar Wochen den Kopf frei zu kriegen. "
                       "Und Marokko während des Ramadan? Klingt erstmal spannend, aber mal ehrlich – den ganzen Tag nichts essen zu können, bis die Sonne untergeht? Das ist jetzt nicht gerade "
                       "der Inbegriff von Genussurlaub. Fazit: Du musst mit! Tauchgänge, Muay Thai, geile Strände, bestes Essen, "
                       "top Gesellschaft – und eine Reise, über die wir noch ewig reden werden. Sag einfach „Ja“ und wir legen los! 😉"
                       "Beste Grüße!! Deine Freunde ")
            c1, c2 = st.columns(2)
            with c1:
                st.image("https://unsplash.com/de/fotos/zwei-auto-rikschas-auf-der-strasse--y3sidWvDxg")
            with c2:
                st.image("https://images.unsplash.com/photo-1496275068113-fff8c90750d1?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fHNlYSUyMEZyaWVuZHN8ZW58MHx8MHx8fDA%3D")
            
            st.write("🚀 Glückwunsch! Du hast das Geheimnis entschlüsselt!")
        else:
            st.error("Falsches Passwort. Versuche es erneut.")


def password_game():
    """Ein einfaches Wortspiel, um das Passwort herauszufinden."""
    st.write("## Spiel: Finde das richtige Wort!")
    st.write("Das Passwort ist ein Anagramm des Wortes 'MEHIGE'!")

    answer = "geheim"
    user_answer = st.text_input("Was ist das richtige Wort?")

    if st.button("Antwort überprüfen"):
        if user_answer.lower() == answer:
            st.success("Richtig! Das Passwort ist: geheim123")
        else:
            st.error("Falsch! Versuche es erneut. Tipp: Das Wort ist gar nicht so schwer zu erraten.")


def main():
    st.title("Geheime Passwort-App")
    page = st.sidebar.selectbox("Navigation", ["Passwort-Eingabe", "Spiel"])

    if page == "Passwort-Eingabe":
        check_password()
    elif page == "Spiel":
        password_game()


if __name__ == "__main__":
    main()
