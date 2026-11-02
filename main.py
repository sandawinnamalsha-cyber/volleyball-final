import flet as ft

def main(page: ft.Page):
    page.title = "Volleyball Pro"
    page.bgcolor = "#0f172a"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # --- State ---
    team_a_name = ft.TextField(value="TEAM A", text_align=ft.TextAlign.CENTER, width=140, color="white", border_color="#38bdf8")
    team_b_name = ft.TextField(value="TEAM B", text_align=ft.TextAlign.CENTER, width=140, color="white", border_color="#fb7185")

    score_a = ft.Text("0", size=90, weight="bold", color="#38bdf8")
    score_b = ft.Text("0", size=90, weight="bold", color="#fb7185")
    
    sets_a_text = ft.Text("Sets: 0", size=18, color="white")
    sets_b_text = ft.Text("Sets: 0", size=18, color="white")
    
    set_history = ft.Column([], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2)
    status_text = ft.Text("First to 25 (win by 2) | Best of 3 Sets", color="#94a3b8", size=12)

    sa = 0
    sb = 0
    sets_a = 0
    sets_b = 0
    history = [] # list of "25-20"

    def check_set_win():
        nonlocal sa, sb, sets_a, sets_b
        # Volleyball rule: 25 points, win by 2
        if (sa >= 25 or sb >= 25) and abs(sa - sb) >= 2:
            winner = "A" if sa > sb else "B"
            history.append(f"{sa}-{sb}")
            set_history.controls.append(ft.Text(f"Set {len(history)}: {team_a_name.value} {sa} - {sb} {team_b_name.value}", color="white", size=14))
            
            if winner == "A":
                sets_a += 1
            else:
                sets_b += 1
            
            sets_a_text.value = f"Sets: {sets_a}"
            sets_b_text.value = f"Sets: {sets_b}"
            
            # Reset points for next set
            sa = 0
            sb = 0
            score_a.value = "0"
            score_b.value = "0"

            # Check match win - best of 3 (first to 2)
            if sets_a == 2 or sets_b == 2:
                match_winner = team_a_name.value if sets_a == 2 else team_b_name.value
                page.dialog = ft.AlertDialog(
                    title=ft.Text(f"🏆 {match_winner} WINS THE MATCH!", size=20, weight="bold"),
                    content=ft.Text(f"Final: {sets_a} - {sets_b}\n" + "\n".join(history)),
                    actions=[ft.TextButton("New Match", on_click=new_match)]
                )
                page.dialog.open = True
            page.update()

    def add_a(e):
        nonlocal sa
        sa+=1
        score_a.value=str(sa)
        check_set_win()
        page.update()

    def sub_a(e):
        nonlocal sa
        if sa>0:
            sa-=1
            score_a.value=str(sa)
            page.update()

    def add_b(e):
        nonlocal sb
        sb+=1
        score_b.value=str(sb)
        check_set_win()
        page.update()

    def sub_b(e):
        nonlocal sb
        if sb>0:
            sb-=1
            score_b.value=str(sb)
            page.update()

    def new_match(e=None):
        nonlocal sa, sb, sets_a, sets_b
        sa=0; sb=0; sets_a=0; sets_b=0
        history.clear()
        score_a.value="0"; score_b.value="0"
        sets_a_text.value="Sets: 0"; sets_b_text.value="Sets: 0"
        set_history.controls.clear()
        if page.dialog:
            page.dialog.open=False
        page.update()

    page.add(
        ft.Column([
            ft.Text("VOLLEYBALL PRO", size=26, weight="bold", color="white"),
            status_text,
            ft.Row([team_a_name, ft.Text("VS", color="white"), team_b_name], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                ft.Column([sets_a_text, score_a, ft.Row([ft.IconButton(ft.icons.REMOVE, on_click=sub_a, icon_color="white"), ft.IconButton(ft.icons.ADD, on_click=add_a, icon_color="#38bdf8", icon_size=30)])], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                ft.Text(":", size=50, color="white"),
                ft.Column([sets_b_text, score_b, ft.Row([ft.IconButton(ft.icons.REMOVE, on_click=sub_b, icon_color="white"), ft.IconButton(ft.icons.ADD, on_click=add_b, icon_color="#fb7185", icon_size=30)])], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            set_history,
            ft.Row([
                ft.ElevatedButton("New Match", on_click=new_match, bgcolor="#1e293b", color="white"),
            ], alignment=ft.MainAxisAlignment.CENTER)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15, scroll=ft.ScrollMode.AUTO)
    )

ft.app(target=main)
